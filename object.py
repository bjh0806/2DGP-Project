from pico2d import *
import random
import game_framework

class Object:
    upground = None
    dir = 0
    Jump = 0
    x = 0
    x2 = 0
    def __init__(self, w = 700, h = 50):
        if Object.upground == None:
            Object.upground = load_image('upground.png')
        self.upgroundw = w
        self.upgroundh = h

    def get_bb(self):
        return self.upgroundw - 90, self.upgroundh - 60, self.upgroundw + 85, self.upgroundh + 60

    def update(self):
        if Object.Jump == 1:
            if Object.dir == 1:
                self.upgroundw -= 7
                if Object.x < Object.x2:
                    self.upgroundh -= 2
                else:
                    self.upgroundh += 2

            else:
                self.upgroundw += 7
                if Object.x < Object.x2:
                    self.upgroundh += 2
                else:
                    self.upgroundh -= 2

        else:
            self.upgroundw -= Object.dir * 7

    def draw(self):
        self.upground.draw(self.upgroundw, self.upgroundh)
        draw_rectangle(*self.get_bb())