from pico2d import *
import random
import game_framework

class Object6:
    heart = None
    def __init__(self):
        if Object6.heart == None:
            Object6.heart = load_image('heart.png')
        self.heartw = [30, 70, 110]
        self.hearth = 570

    def update(self):
        pass

    def draw(self):
        for j in range(0, len(self.heartw)):
            self.heart.draw(self.heartw[j], self.hearth)