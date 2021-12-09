from pico2d import *
import game_world
import game_framework
import random
import collision
import server

class Ball:
    image = None

    def __init__(self, x = 700, y = 115):
        if Ball.image == None:
            Ball.image = load_image('ball.png')
        self.x, self.y = x, y
        self.x2, self.y2 = x, y
        self.frame = 0
        self.fx, self.fy, self.fy2 = 0, 0, 0
        self.i = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def update(self):
        if collision.collide(self, server.mario):
            server.heartcount -= 1
        self.frame = (self.frame + 1 * game_framework.frame_time) % 7
        if self.i == 0:
            self.fx = 0
            self.fy = random.randint(0, 600)
            self.fy2 = random.randint(0, 600)

        t = self.i / 100

        self.x = (1 - t) * 650
        self.y = (1 - t) * 115 + t * self.fy

        self.x2 = (1 - t) * 650
        self.y2 = (1 - t) * 115 + t * self.fy2

        self.i += 4

        if self.i == 104:
            self.i = 0

        if self.x < 0:
            game_world.remove_object(self)

    def draw(self):
        self.image.clip_composite_draw(int(self.frame) * 50, 0, 50, 50, 0, 'h', self.x, self.y, 40, 50)
        self.image.clip_composite_draw(int(self.frame) * 50, 0, 50, 50, 0, 'h', self.x2, self.y2, 40, 50)