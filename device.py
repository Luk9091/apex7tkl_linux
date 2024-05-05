import os
import sys
import traceback

os.environ['LIBUSB_DEBUG'] = 'debug'
import usb.core
from usb.core import USBError
import usb.util

import oled

DEFAULT_LEN = 642

TARGETS = [
    { "name": "apex7",      "idVendor": 0x1038, "idProduct": 0x1612 },
    { "name": "apex7tkl",   "idVendor": 0x1038, "idProduct": 0x1618 },
    { "name": "apexPro",    "idVendor": 0x1038, "idProduct": 0x1610 }
]

def find_device():
    """Find the first matching keyboard device in the TARGETS list"""

    for target in TARGETS:
        try:
            dev = usb.core.find(idVendor = target['idVendor'], idProduct = target['idProduct'])
            if dev is not None:
                return target, dev
        except USBError as e:
            print(f"usb::find({target['name']}) failed: {e}")

    raise Exception("Cannot find a matching device")

def detach_kernel(dev):
    if dev.is_kernel_driver_active(1) == True:
        try:
            print("dev::detach_kernel_driver - interface 1")
            dev.detach_kernel_driver(1)
            return True
        except USBError as e:
            print("dev::detach_kernel_driver failed" + str(e))
    return False

def reattach_kernel(dev, was_detached):
    print("dev::dispose_resources")
    usb.util.dispose_resources(dev)
    if was_detached:
        try:
            print("dev::artach_kernel_driver - interface 1")
            dev.attach_kernel_driver(1)
        except USBError as e:
            print("dev::attach_kernel_driver failed" + str(e))

class Device():
    def __init__ (self):
        self.target = None
        self.handle = None
        self._was_detached = None

    def __enter__ (self):
        self.target, self.handle = find_device()
        self._was_detached = detach_kernel(self.handle)
        return self

    def __exit__ (self, type, value, tb):
        reattach_kernel(self.handle, self._was_detached)


    def pad(self, payload, maxlen=642):
        if len(payload) < maxlen:
            payload += [0x00] * (maxlen - len(payload))
        return payload

    def send(self, wValue = 0x300, reqType = 0x01, payload=None):
        if payload is None:
            raise Exception("payload cannot be null")
        self.handle.ctrl_transfer(0x21,
                0x09,
                wValue,
                reqType,
                payload)

    def send_colors(self, color_payload):
        report = [0x3a, 0x69] + color_payload
        report = self.pad(report, DEFAULT_LEN)
        self.send(0x300, 0x01, report)

    def set_config(self, config_id):
        report = [0x89] + [config_id]
        report = self.pad(report, 20)
        self.send(0x200, 0x01, report)

    def oled_blank(self, filename="/opt/DriversAndScripts/apex7tkl_linux/images/blank.png"):
        self.oled_image(filename)

    def oled_image(self, filename):
        image_data = oled.image_to_payload(filename)
        report = oled.OLED_PREAMBLE + image_data
        self.send(0x300, 0x01, report)

    def oled_text(self, text, font_size):
        image_data = oled.text_payload(text, font_size)
        report = oled.OLED_PREAMBLE + image_data
        self.send(0x300, 0x01, report)

    def oled_time(self):
        image_data = oled.clock_payload()
        report = oled.OLED_PREAMBLE + image_data
        self.send(0x300, 0x01, report)
        

    # def oled_timer(self):
    #     imag
