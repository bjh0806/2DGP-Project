from pico2d import *
import random
import game_framework
import server
import collision

class Object5:
    block = None
    def __init__(self, w = 1075, h = 200):
        if Object5.block == None:
            Object5.block = load_image('block.png')
        self.frame = random.randint(0, 3)
        self.blockw = w
        self.blockh = h

    def get_bb(self):
        return self.blockw - 15, self.blockh - 16.5, self.blockw + 14, self.blockh + 12

    def update(self):
        self.frame = (self.frame + 8 * game_framework.frame_time) % 4
        if server.mario.Jump == 1:
            if server.mario.dir == 1:
                self.blockw -= 7
                if server.mario.x < server.mario.x2:
                    self.blockh -= 2
                else:
                    self.blockh += 2

            else:
                self.blockw += 7
                if server.mario.x < server.mario.x2:
                    self.blockh += 2
                else:
                    self.blockh -= 2

        else:
            self.blockw -= server.mario.dir * 7

    def draw(self):
        self.block.clip_draw(int(self.frame) * 25, 0, 25, 33, self.blockw, self.blockh)
        draw_rectangle(*self.get_bb())