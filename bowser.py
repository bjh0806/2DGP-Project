import random
from pico2d import *
import game_world
import game_framework
import server
import collision
from ball import Ball

class Bowser:
    image = None
    def __init__(self):
        if Bowser.image == None:
            Bowser.image = load_image('bowser.png')
        self.bowserx, self.bowsery = 700, 115
        self.frame = 0
        self.attack = random.randint(0, 1)
        self.timer = 50

    def get_bb(self):
        return self.bowserx - 45, self.bowsery - 35, self.bowserx + 45, self.bowsery + 35

    def fire_ball(self):
        ball = Ball(self.bowserx - 50, self.bowsery)

    def update(self):
        self.frame = (self.frame + 1 * game_framework.frame_time) % 17
        self.timer -= 1
        print(self.timer)
        if self.timer < 0:
            self.timer = 50
            Bowser.fire_ball(self)

    def draw(self):
        if server.hp > 0:
            self.image.clip_composite_draw(int(self.frame) * 100, 1490, 100, 80, 0, 'h', self.bowserx, self.bowsery, 100, 80)