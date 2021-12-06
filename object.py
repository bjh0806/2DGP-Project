from pico2d import *
import random
import game_framework
import server
import collision

class Object:
    upground = None
    def __init__(self, w = 700):
        if Object.upground == None:
            Object.upground = load_image('upground.png')
        self.upgroundw = w
        self.upgroundh = 50

    def get_bb(self):
        return self.upgroundw - 90, self.upgroundh - 60, self.upgroundw + 85, self.upgroundh + 60

    def update(self):
        if collision.collide(self, server.mario):
            if server.mario.Jump == 1:
                server.mario.JumpStop()
            else:
                if server.mario.dir == 1:
                    server.mario.x = object.upgroundw - 110
                else:
                    server.mario.x = object.upgroundw + 105
        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.upgroundh -= 2
            else:
                self.upgroundh += 2

            if server.mario.dir == 1:
                self.upgroundw -= 7
            else:
                self.upgroundw += 7

        else:
            self.upgroundw -= server.mario.dir * 7

    def draw(self):
        self.upground.draw(self.upgroundw, self.upgroundh)