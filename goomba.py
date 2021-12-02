import random
from pico2d import *
import game_world
import game_framework
import server

class Goomba:
    image = None
    def __init__(self):
        if Goomba.image == None:
            Goomba.image = load_image('goomba.png')
        self.goombax, self.goombay = (450, 85)
        self.frame = 0
        self.look = 0
        self.moveg = 0
        
    def get_bb(self):
        return self.goombax - 12, self.goombay - 11, self.goombax + 11, self.goombay + 11

    def update(self):
        self.frame = (self.frame + 16 * game_framework.frame_time) % 8
        if server.mario.Jump == 1:
            if server.mario.dir == 1:
                self.goombax -= 7
                if server.mario.x < server.mario.x2:
                    self.goombay -= 2
                else:
                    self.goombay += 2

            else:
                self.goombax += 7
                if server.mario.x < server.mario.x2:
                    self.goombay += 2
                else:
                    self.goombay -= 2

            if self.look == 0:
                self.moveg -= 2
                self.goombax -= 2

            elif self.look == 1:
                self.moveg += 2
                self.goombax += 2

        else:
            self.goombax -= server.mario.dir * 7
            if self.look == 0:
                self.moveg -= 2
                self.goombax -= 2

            elif self.look == 1:
                self.moveg += 2
                self.goombax += 2

        if self.moveg <= -200:
            self.look = 1
            self.moveg = 0
        elif self.moveg >= 200:
            self.look = 0
            self.moveg = 0
    
    def draw(self):
        if self.look == 0:
            self.image.clip_draw(int(self.frame) * 25, 30, 25, 30, self.goombax, self.goombay)
        else:
            self.image.clip_draw((7 - int(self.frame)) * 25, 0, 25, 30, self.goombax, self.goombay)
        draw_rectangle(*self.get_bb())