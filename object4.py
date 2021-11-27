from pico2d import *
import random
import game_framework

class Object4:
    coin = None
    dir = 0
    Jump = 0
    x = 0
    x2 = 0
    def __init__(self, w = 580, h = 130):
        if Object4.coin == None:
            Object4.coin = load_image('coin.png')
        self.coinw = w
        self.coinh = h

    def get_bb(self):
        return self.coinw - 12.5, self.coinh - 15, self.coinw + 12.5, self.coinh + 15

    def update(self):
        if Object4.Jump == 1:
            if Object4.dir == 1:
                self.coinw -= 7
                if Object4.x < Object4.x2:
                    self.coinh -= 2
                else:
                    self.coinh += 2

            else:
                self.coinw += 7
                if Object4.x < Object4.x2:
                    self.coinh += 2
                else:
                    self.coinh -= 2

        else:
            self.coinw -= Object4.dir * 0.7

    def draw(self):
        self.coin.draw(self.coinw, self.coinh)
        draw_rectangle(*self.get_bb())