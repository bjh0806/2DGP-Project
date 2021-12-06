from pico2d import *
import random
import game_framework
import server

class Object6:
    heart = None
    def __init__(self):
        if Object6.heart == None:
            Object6.heart = load_image('heart.png')
        self.hearth = 570

    def update(self):
        if server.heartcount == 3:
            self.heartw = [30, 70, 110]
        if server.heartcount == 2:
            self.heartw = [30, 70]
        if server.heartcount == 1:
            self.haertw = [30]

    def draw(self):
        if server.heartcount != 0:
            for j in range(0, len(self.heartw)):
                self.heart.draw(self.heartw[j], self.hearth)