from pico2d import *
import game_world
import game_framework
import random
import collision
import server

class Fire:
    image = None

    def __init__(self, x = 700, y = 115, velocity = 1):
        if Fire.image == None:
            Fire.image = load_image('fire.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def update(self):
        if collision.collide(self, server.mario):
            pass
        self.frame = (self.frame + 1 * game_framework.frame_time) % 2

        self.x += self.velocity

        if self.x > 800 or self.x < 0:
            game_world.remove_object(self)

    def draw(self):
        if self.velocity >= 0:
            self.image.clip_draw(int(self.frame) * 70, 50, 70, 50, self.x, self.y)
        else:
            self.image.clip_draw((1 - int(self.frame)) * 70, 0, 70, 50, self.x, self.y)