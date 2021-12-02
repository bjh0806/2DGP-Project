from pico2d import *
import random
import game_framework
import server
import collision

class Object2:
    upground2 = None
    def __init__(self, w = 850, h = 70):
        if Object2.upground2 == None:
            Object2.upground2 = load_image('upground_double.png')
        self.upground2w = w
        self.upground2h = h

    def get_bb(self):
        return self.upground2w - 90, self.upground2h - 100, self.upground2w + 85, self.upground2h + 100

    def update(self):
        if server.mario.Jump == 1:
            if server.mario.dir == 1:
                self.upground2w -= 7
                if server.mario.x < server.mario.x2:
                    self.upground2h -= 2
                else:
                    self.upground2h += 2

            else:
                self.upground2w += 7
                if server.mario.x < server.mario.x2:
                    self.upground2h += 2
                else:
                    self.upground2h -= 2

        else:
            self.upground2w -= server.mario.dir * 7

    def draw(self):
        self.upground2.draw(self.upground2w, self.upground2h)
        draw_rectangle(*self.get_bb())