import random
from pico2d import *
import game_world
import game_framework

class Goomba:
    image = None
    Jump = 0
    right = 1
    left = 0
    dir = 0
    x = 0
    x2 = 0
    def __init__(self):
        if Goomba.image == None:
            Goomba.image = load_image('goomba.png')
        self.goombax, self.goombay = 450, 85
        self.frame = 0
        
    def get_bb(self):
        pass

    def update(self):
        self.frame = (self.frame + 16 * game_framework.frame_time) % 8
        if Goomba.Jump == 1:
            if Goomba.right == 1:
                self.goombax -= 7
                if Goomba.x < Goomba.x2:
                    self.goombay -= 2
                else:
                    self.goombay += 2

            elif Goomba.left == 1:
                self.goombax += 7
                if Goomba.x < Goomba.x2:
                    self.goombay += 2
                else:
                    self.goombay -= 2

        else:
            self.goombax -= Goomba.dir * 7
    
    def draw(self):
        self.image.clip_draw(int(self.frame) * 25, 30, 25, 30, self.goombax, self.goombay)