from pico2d import *
import random
import game_framework
import server
import collision

class Object:
    upground = None
    def __init__(self, w = 700, h = 50):
        if Object.upground == None:
            Object.upground = load_image('upground.png')
        self.upgroundw = w
        self.upgroundh = h

    def get_bb(self):
        return self.upgroundw - 90, self.upgroundh - 60, self.upgroundw + 85, self.upgroundh + 60

    def update(self):
        for object in server.objects1.copy():
            if collision.collide(object, server.mario):
                server.mario.stop1()
        if server.mario.Jump == 1:
            if server.mario.dir == 1:
                self.upgroundw -= 7
                if server.mario.x < server.mario.x2:
                    self.upgroundh -= 2
                else:
                    self.upgroundh += 2

            else:
                self.upgroundw += 7
                if server.mario.x < server.mario.x2:
                    self.upgroundh += 2
                else:
                    self.upgroundh -= 2

        else:
            pass
            # self.upgroundw -= server.mario.dir * 7

    def draw(self):
        self.upground.draw(self.upgroundw, self.upgroundh)
        draw_rectangle(*self.get_bb())