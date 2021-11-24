from pico2d import *
import random
import game_framework

class Object4:
    coin = None
    dir = 0
    Jump = 0
    x = 0
    x2 = 0
    def __init__(self):
        if Object4.coin == None:
            Object4.coin = load_image('coin.png')
        self.coinw = [580, 610, 640, 740, 770, 800, 1300, 1330, 1360, 1390, 2175, 2205, 2235, 2265]
        self.coinh = [130, 160, 180, 180, 210, 230, 160, 190, 190, 160, 160, 190, 190, 160]

    def get_bb(self):
        for m in range(0, len(self.coinw)):
            return self.coinw[m] - 12.5, self.coinh[m] - 15, self.coinw[m] + 12.5, self.coinh[m] + 15

    def update(self):
        if Object4.Jump == 1:
            if Object4.dir == 1:
                for m in range(0, len(self.coinw)):
                    self.coinw[m] -= 7
                if Object4.x < Object4.x2:
                    for m in range(0, len(self.coinh)):
                        self.coinh[m] -= 2
                else:
                    for m in range(0, len(self.coinh)):
                        self.coinh[m] += 2

            else:
                for m in range(0, len(self.coinw)):
                    self.coinw[m] += 7
                if Object4.x < Object4.x2:
                    for m in range(0, len(self.coinh)):
                        self.coinh[m] += 2
                else:
                    for m in range(0, len(self.coinh)):
                        self.coinh[m] -= 2

        else:
            for m in range(0, len(self.coinw)):
                self.coinw[m] -= Object4.dir * 7

    def draw(self):
        for m in range(0, len(self.coinw)):
            self.coin.draw(self.coinw[m], self.coinh[m])
        draw_rectangle(*self.get_bb())