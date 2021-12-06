from pico2d import *
import random
import game_framework
import server
import collision
import game_world

class Object4:
    coin = None
    def __init__(self, w = 580, h = 130):
        if Object4.coin == None:
            Object4.coin = load_image('coin.png')
        self.coinw = w
        self.coinh = h

    def get_bb(self):
        return self.coinw - 12.5, self.coinh - 15, self.coinw + 12.5, self.coinh + 15

    def update(self):
        if collision.collide(self, server.mario):
            game_world.remove_object(self)
        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.coinh -= 2
            else:
                self.coinh += 2

            if server.mario.dir == 1:
                self.coinw -= 7
            else:
                self.coinw += 7

        else:
            self.coinw -= server.mario.dir * 7

    def draw(self):
        self.coin.draw(self.coinw, self.coinh)