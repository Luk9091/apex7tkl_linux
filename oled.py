from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from clock import get_time
# from clock import timer()


full = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\xfc\x00\x3f\xfe\x00\x70\x1c\x00\x07\x03\x80\x00\xe0" \
"\xc0\x00\x03\xff\x00\x3f\xff\x80\x70\x1e\x00\x0f\x03\xc0\x01\xe0" \
"\xc0\x00\x07\xff\x80\x3f\xff\xc0\x70\x1e\x00\x0f\x03\xc0\x01\xe0" \
"\xc0\x00\x0f\xcf\xc0\x3c\x07\xc0\x70\x1f\x00\x1f\x03\xe0\x03\xe0" \
"\xc0\x00\x0f\x01\xe0\x38\x01\xe0\x70\x1f\x00\x1f\x03\xe0\x03\xe0" \
"\xc0\x00\x1e\x01\xe0\x38\x01\xe0\x70\x1f\x80\x1f\x03\xf0\x03\xe0" \
"\xc0\x00\x1e\x00\xf0\x38\x01\xe0\x70\x1f\x80\x3f\x03\xf0\x07\xe0" \
"\xc0\x00\x1c\x00\x00\x38\x01\xe0\x70\x1f\xc0\x3f\x03\xf8\x07\xe0" \
"\xc0\x00\x1c\x00\x00\x38\x01\xe0\x70\x1f\xc0\x7f\x03\xf8\x0f\xe0" \
"\xc0\x00\x1c\x00\x00\x38\x01\xe0\x70\x1d\xc0\x77\x03\xb8\x0e\xe0" \
"\xc0\x00\x1c\x00\x00\x3c\x07\xc0\x70\x1c\xe0\xf7\x03\x9c\x1e\xe0" \
"\xc0\x00\x1c\x00\x00\x3f\xff\xc0\x70\x1c\xe0\xe7\x03\x9c\x1c\xe0" \
"\xc0\x00\x1c\x0f\xf0\x3f\xff\x80\x70\x1c\x71\xe7\x03\x8e\x3c\xe0" \
"\xc0\x00\x1c\x0f\xf0\x3f\xfe\x00\x70\x1c\x71\xc7\x03\x8e\x38\xe0" \
"\xc0\x00\x1c\x0f\xf0\x38\x1e\x00\x70\x1c\x79\xc7\x03\x8f\x38\xe0" \
"\xc0\x00\x1c\x00\x70\x38\x0e\x00\x70\x1c\x3b\x87\x03\x87\x70\xe0" \
"\xc0\x00\x1c\x00\x70\x38\x0f\x00\x70\x1c\x3f\x87\x03\x87\xf0\xe0" \
"\xc0\x00\x1c\x00\xf0\x38\x07\x00\x70\x1c\x1f\x87\x03\x83\xf0\xe0" \
"\xc0\x00\x1c\x00\xf0\x38\x07\x80\x70\x1c\x1f\x07\x03\x83\xe0\xe0" \
"\xc0\x00\x1e\x00\xe0\x38\x07\x80\x70\x1c\x0f\x07\x03\x81\xe0\xe0" \
"\xc0\x00\x0f\x01\xe0\x38\x03\xc0\x70\x1c\x0e\x07\x03\x81\xc0\xe0" \
"\xc0\x00\x0f\xc7\xc0\x38\x03\xc0\x70\x1c\x06\x07\x03\x80\xc0\xe0" \
"\xc0\x00\x07\xff\xc0\x38\x01\xe0\x70\x1c\x00\x07\x03\x80\x00\xe0" \
"\xc0\x00\x03\xff\x00\x38\x01\xe0\x70\x1c\x00\x07\x03\x80\x00\xe0" \
"\xc0\x00\x00\xfc\x00\x38\x00\xf0\x70\x1c\x00\x07\x03\x80\x00\xe0" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
"\xc1\x00"

OLED_WIDTH = 128
OLED_HEIGHT = 40

full = [ord(x) for x in full]

#OLED_PREAMBLE = [0x65, 0xfc]
OLED_PREAMBLE = [0x65]

#print("[%s]" % (", ".join(map(hex, full))), len(full))

def text_payload(text, font_size = 16):
    im = Image.new("1", (OLED_WIDTH, OLED_HEIGHT))

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Font/DejaVuSansMono.ttf", font_size)

    draw.text((1,0), text, fill=(255), font=font)

    return _pixels_to_payload(im)

def clock_payload():
    img = Image.new('1', (OLED_WIDTH, OLED_HEIGHT))
    
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Font/DejaVuSansMono.ttf", 42)
    draw.text((-1, -3), get_time(), font=font, fill=(255))

    return _pixels_to_payload(img)

def timer_payload():
    img = Image.new('1', (OLED_WIDTH, OLED_HEIGHT))

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Font/DejaVuSansMono.ttf", 42)

def _pixels_to_payload(im):
    pix = im.load()

    payload_bin = []
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            val = 0
            if pix[x, y] > 127:
                val = 1
            if len(payload_bin) == 0 or len(payload_bin[-1]) == 8:
                payload_bin.append("")
            payload_bin[-1] += str(val)

    payload_bin = [int(b, 2) for b in payload_bin]
    return payload_bin

def image_to_payload(filename="payload.png"):
    im = Image.open(filename)
    if im.size[0] != OLED_WIDTH or im.size[1] != OLED_HEIGHT:
        im.resize( (OLED_WIDTH, OLED_HEIGHT) )

    im = im.convert("1")
    return _pixels_to_payload(im)

def payload_to_image(payload, filename="payload.png"):
    im = Image.new("1", (OLED_WIDTH, OLED_HEIGHT))

    payload_bin = "".join(map(lambda x: bin(x)[2:].rjust(8, "0"), payload))

    lines = []
    while len(payload_bin) > 0:
        lines.append( payload_bin[0:OLED_WIDTH] )
        payload_bin = payload_bin[OLED_WIDTH:]

    pix = im.load()

    for y, linedata in enumerate(lines):
        for x, value in enumerate(linedata):
            pix[x, y] = int(value == '1')

    im.save(filename)

def printimage(payload):
    for lineidx, line in enumerate(toimage(payload)):
        print(str(lineidx).rjust(2), line)

def toimage(payload):
    # len(payload) without preamble is 640
    # 640*2*4 = 5120, 5120/40 = 128
    # print("[%s]" % (", ".join(payload)), len(payload))

    payload_bin = "".join(map(lambda x: bin(x)[2:].rjust(8, "0"), payload))

    lines = []
    while len(payload_bin) > 0:
        lines.append( payload_bin[0:OLED_WIDTH] )
        payload_bin = payload_bin[OLED_WIDTH:]

    imglines = []
    for lineidx, line in enumerate(lines):
        imglines.append( line.replace("0", " "))
    return imglines

#printimage(full)
#payload_to_image(full, "payload.png")
#loaded = image_to_payload("payload.png")
#printimage(loaded)
#
#printimage(text_payload("Hello World\nLine 2\nLine3"))
#printimage(text_payload("Hello World\nLine 2\nOverflow 12345678901234567890"))
#
