from pico2d import *
import random
import game_framework

class Object3:
    random_box = None
    dir = 0
    Jump = 0
    x = 0
    x2 = 0
    def __init__(self):
        if Object3.random_box == None:
            Object3.random_box = load_image('random_box.png')
        self.randomframe = random.randint(0, 3)
        self.random_boxw = [300, 400, 425, 855, 1100, 1600, 1825, 2000, 2025]
        self.random_boxh = [200, 200, 200, 300, 200, 200, 200, 200, 200]

    def get_bb(self):
        for j in range(0, len(self.random_boxw)):
            return self.random_boxw[j] - 15, self.random_boxh[j] - 16.5, self.random_boxw[j] + 14, self.random_boxh[j] + 12

    def update(self):
        self.randomframe = (self.randomframe + 8 * game_framework.frame_time) % 4
        if Object3.Jump == 1:
            if Object3.dir == 1:
                for j in range(0, len(self.random_boxw)):
                    self.random_boxw[j] -= 7
                if Object3.x < Object3.x2:
                    for j in range(0, len(self.random_boxh)):
                        self.random_boxh[j] -= 2
                else:
                    for j in range(0, len(self.random_boxh)):
                        self.random_boxh[j] += 2

            else:
                for j in range(0, len(self.random_boxw)):
                    self.random_boxw[j] += 7
                if Object3.x < Object3.x2:
                    for j in range(0, len(self.random_boxh)):
                        self.random_boxh[j] += 2
                else:
                    for j in range(0, len(self.random_boxh)):
                        self.random_boxh[j] -= 2

        else:
            for j in range(0, len(self.random_boxw)):
                self.random_boxw[j] -= Object3.dir * 7

    def draw(self):
        for j in range(0, len(self.random_boxw)):
            self.random_box.clip_draw(int(self.randomframe) * 25, 0, 25, 33, self.random_boxw[j], self.random_boxh[j])
        draw_rectangle(*self.get_bb())