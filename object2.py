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
        return self.upground2w - 85, self.upground2h - 100, self.upground2w + 85, self.upground2h + 95

    def update(self):
        for object2 in server.objects2.copy():
            if collision.collide(object2, server.mario):
                if server.mario.Jump == 1:
                    server.mario.JumpStop()
                else:
                    if server.mario.dir == 1:
                        server.mario.x = object2.upground2w - 105
                    else:
                        server.mario.x = object2.upground2w + 105
        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.upground2h -= 2
            else:
                self.upground2h += 2

            if server.mario.dir == 1:
                self.upground2w -= 7
            else:
                self.upground2w += 7

        else:
            self.upground2w -= server.mario.dir * 7

    def draw(self):
        self.upground2.draw(self.upground2w, self.upground2h)