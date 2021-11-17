from pico2d import *
import random
import game_framework

class Object5:
    block = None
    dir = 0
    Jump = 0
    right = 1
    left = 0
    x = 0
    x2 = 0
    def __init__(self):
        if Object5.block == None:
            Object5.block = load_image('block.png')
        self.frame = random.randint(0, 3)
        self.blockw = [1075, 1124]
        self.blockh = [200, 200]

    def get_bb(self):
        for j in range(0, len(self.blockw)):
            return self.blockw[j] - 15, self.blockh[j] - 16.5, self.blockw[j] + 14, self.blockh[j] + 12

    def update(self):
        self.frame = (self.frame + 8 * game_framework.frame_time) % 4
        if Object5.Jump == 1:
            if Object5.right == 1:
                for j in range(0, len(self.blockw)):
                    self.blockw[j] -= 7
                if Object5.x < Object5.x2:
                    for j in range(0, len(self.blockh)):
                        self.blockh[j] -= 2
                else:
                    for j in range(0, len(self.blockh)):
                        self.blockh[j] += 2

            elif Object5.left == 1:
                for j in range(0, len(self.blockw)):
                    self.blockw[j] += 7
                if Object5.x < Object5.x2:
                    for j in range(0, len(self.blockh)):
                        self.blockh[j] += 2
                else:
                    for j in range(0, len(self.blockh)):
                        self.blockh[j] -= 2

        else:
            for j in range(0, len(self.blockw)):
                self.blockw[j] -= Object5.dir * 7

    def draw(self):
        for j in range(0, len(self.blockw)):
            self.block.clip_draw(int(self.frame) * 25, 0, 25, 33, self.blockw[j], self.blockh[j])
        draw_rectangle(*self.get_bb())