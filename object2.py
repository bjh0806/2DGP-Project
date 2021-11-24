from pico2d import *
import random
import game_framework

class Object2:
    upground2 = None
    dir = 0
    Jump = 0
    x = 0
    x2 = 0
    def __init__(self, w = 850, h = 70):
        if Object2.upground2 == None:
            Object2.upground2 = load_image('upground_double.png')
        self.upground2w = w
        self.upground2h = h

    def get_bb(self):
        return self.upground2w - 90, self.upground2h - 100, self.upground2w + 85, self.upground2h + 100

    def update(self):
        if Object2.Jump == 1:
            if Object2.dir == 1:
                self.upground2w -= 7
                if Object2.x < Object2.x2:
                    self.upground2h -= 2
                else:
                    self.upground2h += 2

            else:
                self.upground2w += 7
                if Object2.x < Object2.x2:
                    self.upground2h += 2
                else:
                    self.upground2h -= 2

        else:
            self.upground2w -= Object2.dir * 7

    def draw(self):
        self.upground2.draw(self.upground2w, self.upground2h)
        draw_rectangle(*self.get_bb())