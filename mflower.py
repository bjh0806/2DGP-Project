import random
from pico2d import *
import game_world
import game_framework
import server
import collision

class Mflower:
    image = None

    def __init__(self, x = 450):
        if Mflower.image == None:
            Mflower.image = load_image('Mflower.png')
        self.mflowerx, self.mflowery = x, 100
        self.frame = random.randint(0, 7)
        self.look = random.randint(0, 1)
        self.moveg = 0

    def get_bb(self):
        return self.mflowerx - 12, self.mflowery - 11, self.mflowerx + 11, self.mflowery + 11

    def update(self):
        self.frame = (self.frame + 8 * game_framework.frame_time) % 8
        if collision.collide(self, server.mario):
            game_world.remove_object(self)
        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.mflowery -= 2
            else:
                self.mflowery += 2

            if server.mario.dir == 1:
                self.mflowerx -= 7

            else:
                self.mflowerx += 7

        else:
            self.mflowerx -= server.mario.dir * 7

    def draw(self):
        if self.look == 0:
            self.image.clip_draw(int(self.frame) * 40, 40, 40, 40, self.mflowerx, self.mflowery)
        else:
            self.image.clip_draw((7 - int(self.frame)) * 40, 0, 40, 40, self.mflowerx, self.mflowery)