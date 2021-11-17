from pico2d import *
import random
import game_framework

class Object:
    upground = None
    dir = 0
    Jump = 0
    right = 1
    left = 0
    x = 0
    x2 = 0
    def __init__(self):
        if Object.upground == None:
            Object.upground = load_image('upground.png')
        self.upgroundh = 50
        self.upgroundw = [700]

    def get_bb(self):
        for k in range(0, len(self.upgroundw)):
            return self.upgroundw[k] - 90, self.upgroundh - 60, self.upgroundw[k] + 85, self.upgroundh + 60

    def update(self):
        if Object.Jump == 1:
            if Object.right == 1:
                for k in range(0, len(self.upgroundw)):
                    self.upgroundw[k] -= 7
                if Object.x < Object.x2:
                    self.upgroundh -= 2
                else:
                    self.upgroundh += 2

            elif Object.left == 1:
                for k in range(0, len(self.upgroundw)):
                    self.upgroundw[k] += 7
                if Object.x < Object.x2:
                    self.upgroundh += 2
                else:
                    self.upgroundh -= 2

        else:
            for k in range(0, len(self.upgroundw)):
                self.upgroundw[k] -= Object.dir * 7

    def draw(self):
        for k in range(0, len(self.upgroundw)):
            self.upground.draw(self.upgroundw[k], self.upgroundh)
        draw_rectangle(*self.get_bb())