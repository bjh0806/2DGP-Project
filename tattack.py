import random
from pico2d import *
import game_world
import game_framework
import server
import collision

class Tattack:
    image = None

    def __init__(self, x=450):
        if Tattack.image == None:
            Tattack.image = load_image('Tattack.png')
        self.tattackx, self.tattacky = x, 85
        self.frame = random.randint(0, 7)
        self.look = random.randint(0, 1)
        self.moveg = 0

    def get_bb(self):
        return self.tattackx - 12, self.tattacky - 11, self.tattackx + 11, self.tattacky + 11

    def update(self):
        self.frame = (self.frame + 8 * game_framework.frame_time) % 8
        for tattack in server.tattacks.copy():
            if self.tattackx < 400 or self.tattackx > 1200:
                game_world.remove_object(tattack)
        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.tattacky -= 2
            else:
                self.tattacky += 2

            if server.mario.dir == 1:
                self.tattackx -= 10

            else:
                self.tattackx += 10

            if self.look == 0:
                self.moveg -= 2
                self.tattackx -= 3

            elif self.look == 1:
                self.moveg += 2
                self.tattackx += 3

        else:
            self.tattackx -= server.mario.dir * 10
            if self.look == 0:
                self.moveg -= 2
                self.tattackx -= 3

            elif self.look == 1:
                self.moveg += 2
                self.tattackx += 3

        if self.moveg <= -200:
            self.look = 1
            self.moveg = 0
        elif self.moveg >= 200:
            self.look = 0
            self.moveg = 0

    def draw(self):
        if self.look == 0:
            self.image.clip_draw(int(self.frame) * 25, 25, 25, 25, self.tattackx, self.tattacky)
        else:
            self.image.clip_draw((8 - int(self.frame)) * 25, 0, 25, 25, self.tattackx, self.tattacky)
        draw_rectangle(*self.get_bb())