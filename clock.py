from PIL import Image, ImageDraw, ImageFont
import time

def get_time():
    current_time = time.asctime()
    current_time = current_time.split(' ')
    current_time.remove('')
    current_time = current_time[3][:-3]
    return current_time

def get_sec():
    current_time = time.asctime()
    current_time = current_time.split(' ')[3][-2:]
    return current_time


# def get_time_img():
#     img = Image.new('1', (128, 40), "black")
#     font = ImageFont.truetype("Font/DejaVuSansMono.ttf", 42)
#     text = ImageDraw.Draw(img)
#     text.text((-1, -3), get_time(), font=font, fill=1)
#     return img

def wait(wait):
    time.sleep(wait)


# def timer(timer):

if __name__ == "__main__":
    # print(get_time())
    print(get_time())