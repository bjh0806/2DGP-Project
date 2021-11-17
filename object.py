from pico2d import *
import random
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION4 = 4

class Object:
    upground = None
    upground2 = None
    random_box = None
    coin = None

    def __init__(self):
        if Object.random_box == None:
            Object.random_box = load_image('random_box.png')
        if Object.upground == None:
            Object.upground = load_image('upground.png')
        if Object.upground2 == None:
            Object.upground2 = load_image('upground_double.png')
        if Object.coin == None:
            Object.coin = load_image('coin.png')
        self.randomframe = random.randint(0, 3)
        self.upgroundh = 50
        self.upground2h = 70
        self.Jump = 0
        self.right = 1
        self.left = 0
        self.x = 0
        self.x2 = 0
        self.dir = 0
        self.random_boxw = [300, 400, 425, 855, 1100, 1900, 2025]
        self.random_boxh = [200, 200, 200, 300, 200, 200, 200]
        self.upgroundw = [700]
        self.upgroundh = 50
        self.upground2w = [850]
        self.upground2h = 70
        self.coinw = [580, 610, 640, 740, 770, 800]
        self.coinh = [130, 160, 180, 180, 210, 230]

    def update_random_box(self):
        self.randomframe = (self.randomframe + 8 * game_framework.frame_time) % 4

    def update(self):
        if self.Jump == 1:
            if self.right == 1:
                for j in range(0, len(self.random_boxw)):
                    self.random_boxw[j] -= 7
                for k in range(0, len(self.upgroundw)):
                    self.upgroundw[k] -= 7
                for l in range(0, len(self.upground2w)):
                    self.upground2w[l] -= 7
                for m in range(0, len(self.coinw)):
                    self.coinw[m] -= 7
                if self.x < self.x2:
                    for j in range(0, len(self.random_boxh)):
                        self.random_boxh[j] -= 2
                    for m in range(0, len(self.coinh)):
                        self.coinh[m] -= 2
                    self.upgroundh -= 2
                    self.upground2h -= 2
                else:
                    for j in range(0, len(self.random_boxh)):
                        self.random_boxh[j] += 2
                    for m in range(0, len(self.coinh)):
                        self.coinh[m] += 2
                    self.upgroundh += 2
                    self.upground2h += 2

            elif self.left == 1:
                for j in range(0, len(self.random_boxw)):
                    self.random_boxw[j] += 7
                for k in range(0, len(self.upgroundw)):
                    self.upgroundw[k] += 7
                for l in range(0, len(self.upground2w)):
                    self.upground2w[l] += 7
                for m in range(0, len(self.coinw)):
                    self.coinw[m] += 7
                if self.x < self.x2:
                    for j in range(0, len(self.random_boxh)):
                        self.random_boxh[j] += 2
                    for m in range(0, len(self.coinh)):
                        self.coinh[m] += 2
                    self.upgroundh += 2
                    self.upground2h += 2
                else:
                    for j in range(0, len(self.random_boxh)):
                        self.random_boxh[j] -= 2
                    for m in range(0, len(self.coinh)):
                        self.coinh[m] -= 2
                    self.upgroundh -= 2
                    self.upground2h -= 2

        else:
            for j in range(0, len(self.random_boxw)):
                self.random_boxw[j] -= self.dir * 7
            for k in range(0, len(self.upgroundw)):
                self.upgroundw[k] -= self.dir * 7
            for l in range(0, len(self.upground2w)):
                self.upground2w[l] -= self.dir * 7
            for m in range(0, len(self.coinw)):
                self.coinw[m] -= self.dir * 7

    def draw_random_box(self):
        for j in range(0, len(self.random_boxw)):
            self.random_box.clip_draw(int(self.randomframe) * 25, 0, 25, 33, self.random_boxw[j], self.random_boxh[j])

    def draw_upground(self):
        for k in range(0, len(self.upgroundw)):
            self.upground.draw(self.upgroundw[k], self.upgroundh)

    def draw_upground2(self):
        for l in range(0, len(self.upground2w)):
            self.upground2.draw(self.upground2w[l], self.upground2h)

    def draw_coin(self):
        for m in range(0, len(self.coinw)):
            self.coin.draw(self.coinw[m], self.coinh[m])