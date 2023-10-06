import random
# from dataclasses import dataclass



# @dataclass
class Keyboard:
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]


    def __init__(self):
        pass

    def get_key(self, x, y):
        if(abs(y) >= len(keyboard)):
            raise Exception("This y index dont exist")

        return self.keyboard[y][x]



keyboard = Keyboard()
print(keyboard.get_key(0, -1))



