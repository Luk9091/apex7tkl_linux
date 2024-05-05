from PIL import Image, ImageDraw, ImageFont
import time

def get_time():
    local_time = time.localtime()
    current_time = time.strftime("%H:%M", local_time)
    return current_time

def get_sec():
    current_time = time.asctime()
    current_time = current_time.split(' ')[3][-2:]
    return current_time


def wait(wait):
    time.sleep(wait)



if __name__ == "__main__":
    print(get_time())