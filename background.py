from pico2d import *
import random
import game_framework
import server
import collision

class Background:
    image = None
    def __init__(self):
        if Background.image == None:
            Background.image = load_image('boss_background.png')
        self.w = 400
        self.h = 300

    def get_bb(self):
        return 0, self.h - 300, 800, self.h - 230

    def update(self):
        if collision.collide(self, server.mario):
            server.mario.JumpStop()

    def draw(self):
        self.image.draw(self.w, self.h)