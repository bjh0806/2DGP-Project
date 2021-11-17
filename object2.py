from pico2d import *
import random
import game_framework

class Object2:
    upground2 = None
    dir = 0
    Jump = 0
    right = 1
    left = 0
    x = 0
    x2 = 0
    def __init__(self):
        if Object2.upground2 == None:
            Object2.upground2 = load_image('upground_double.png')
        self.upground2w = [850, 2500]
        self.upground2h = 70

    def get_bb(self):
        for l in range(0, len(self.upground2w)):
            return self.upground2w[l] - 90, self.upground2h - 100, self.upground2w[l] + 85, self.upground2h + 100

    def update(self):
        if Object2.Jump == 1:
            if Object2.right == 1:
                for l in range(0, len(self.upground2w)):
                    self.upground2w[l] -= 7
                if Object2.x < Object2.x2:
                    self.upground2h -= 2
                else:
                    self.upground2h += 2

            elif Object2.left == 1:
                for l in range(0, len(self.upground2w)):
                    self.upground2w[l] += 7
                if Object2.x < Object2.x2:
                    self.upground2h += 2
                else:
                    self.upground2h -= 2

        else:
            for l in range(0, len(self.upground2w)):
                self.upground2w[l] -= Object2.dir * 7

    def draw(self):
        for l in range(0, len(self.upground2w)):
            self.upground2.draw(self.upground2w[l], self.upground2h)
        draw_rectangle(*self.get_bb())