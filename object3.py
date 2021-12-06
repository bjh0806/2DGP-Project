from pico2d import *
import random
import game_framework
import server
import collision

class Object3:
    random_box = None
    block = None
    def __init__(self, w = 300, h = 200):
        if Object3.random_box == None:
            Object3.random_box = load_image('random_box.png')
        if Object3.block == None:
            Object3.block = load_image('block.png')
        self.randomframe = random.randint(0, 3)
        self.random_boxw = w
        self.random_boxh = h
        self.eat = 0

    def get_bb(self):
        return self.random_boxw - 15, self.random_boxh - 16.5, self.random_boxw + 14, self.random_boxh + 12

    def update(self):
        self.randomframe = (self.randomframe + 8 * game_framework.frame_time) % 4
        self.count = 0
        if collision.collide(self, server.mario):
            self.eat = 1

        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.random_boxh -= 2
            else:
                self.random_boxh += 2

            if server.mario.dir == 1:
                self.random_boxw -= 7
            else:
                self.random_boxw += 7

        else:
            self.random_boxw -= server.mario.dir * 7

    def draw(self):
        if self.eat == 0:
            self.random_box.clip_draw(int(self.randomframe) * 25, 0, 25, 33, self.random_boxw, self.random_boxh)
        else:
            self.block.clip_draw(int(self.randomframe) * 25, 0, 25, 33, self.random_boxw, self.random_boxh)