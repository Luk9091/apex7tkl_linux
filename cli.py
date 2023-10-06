#!/usr/bin/env python3

import sys

import keys
import colors
import device
import clock



def set_config(config_id):
    with device.Device() as dev:
        dev.set_config(int(config_id))

def oled_blank():
    with device.Device() as dev:
        dev.oled_blank()

def oled_update(filename):
    with device.Device() as dev:
        dev.oled_image(filename)

def oled_time(wait = 60):
    with device.Device() as dev:
        dev.oled_time()
        clock.wait(wait- int(clock.get_sec()))
        while(1):
            dev.oled_time()
            clock.wait(wait)



def oled_text(*args):
    font_size = 16
    to_text = []
    for arg in args:
        if(arg.isnumeric()):
            font_size = int(arg)
        else:
            to_text.append(arg)

    text = "\n".join(to_text).strip()
    print(text)
    with device.Device() as dev:
        dev.oled_text(text, font_size)


def set_colors(*colordef):
    l = list(colordef)

    defs = {}

    while len(l) > 0:
        key_target = l.pop(0).split(",")
        col = l.pop(0)

        for tgt in key_target:
            if tgt == '--':
                # special: applies color to all yet unused colors
                for keycode in keys.others(defs.keys()):
                    defs[keycode] = colors.get(col)
            for keycode in keys.get(tgt):
                if keycode is None:
                    continue
                defs[keycode] = colors.get(col)

    if len(defs) == 0:
        raise Exception("could not determine any color definitions")

    COLOR_PAYLOAD = []
    for keycode, color in defs.items():
        COLOR_PAYLOAD += [keycode]
        COLOR_PAYLOAD += color

    with device.Device() as dev:
        dev.send_colors(COLOR_PAYLOAD)

COMMANDS = {
        "config":       {"minargs": 1, "handler": set_config},
        "oled":         {"minargs": 1, "handler": oled_update},
        "oledblank":    {"minargs": 0, "handler": oled_blank},
        "oledtext":     {"minargs": 1, "handler": oled_text},
        "color":        {"minargs": 2, "handler": set_colors},
        "clock":        {"minargs": 0, "handler": oled_time},
        # "timer": {"minargs": 1, "handler": timer}
        }

if __name__ == "__main__":
    args = sys.argv[1:]
    print(args, len(args))

    if len(args) == 0:
        print("missing command. valid: %s" % ", ".join(COMMANDS.keys()))
        sys.exit(1)

    command = args[0]
    args = args[1:]

    if 'minargs' in COMMANDS[command] and len(args) < COMMANDS[command]['minargs']:
        print('command "%s" requires at least %s arguments' % ( command, COMMANDS[command]['minargs'] ))
        sys.exit(1)

    COMMANDS[command]['handler'](*args)
