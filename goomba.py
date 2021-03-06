import random
from pico2d import *
import game_world
import game_framework
import server
import collision

class Goomba:
    image = None
    def __init__(self, x = 450):
        if Goomba.image == None:
            Goomba.image = load_image('goomba.png')
        self.goombax, self.goombay = x, 85
        self.frame = random.randint(0, 7)
        self.look = random.randint(0, 1)
        self.moveg = 0
        server.goomba_sound = load_wav('goomba_sound.wav')
        server.goomba_sound.set_volume(64)
        
    def get_bb(self):
        return self.goombax - 12, self.goombay - 11, self.goombax + 11, self.goombay + 11

    def update(self):
        self.frame = (self.frame + 8 * game_framework.frame_time) % 8
        if collision.collide(self, server.mario):
            server.goomba_sound.play()
            game_world.remove_object(self)
        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.goombay -= 2
            else:
                self.goombay += 2

            if server.mario.dir == 1:
                self.goombax -= 7

            else:
                self.goombax += 7

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