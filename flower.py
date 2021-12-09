from pico2d import *
import random
import game_framework
import server
import collision
import game_world

class Flower:
    image = None
    def __init__(self, w = 462.5, h = 260):
        if Flower.image == None:
            Flower.image = load_image('flower.png')
        self.flowerw = w
        self.flowerh = h
        server.flower_sound = load_wav('strong_sound.wav')
        server.flower_sound.set_volume(64)

    def get_bb(self):
        return self.flowerw - 12.5, self.flowerh - 15, self.flowerw + 12.5, self.flowerh + 15

    def update(self):
        if collision.collide(self, server.mario):
            server.flower_sound.play()
            game_world.remove_object(self)
            server.mode = 1

    def draw(self):
        self.image.draw(self.flowerw, self.flowerh)