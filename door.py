from pico2d import *
import random
import game_framework
import server
import collision
import main2_state

class Door:
    image = None
    def __init__(self):
        if Door.image == None:
            Door.image = load_image('door.png')
        self.doorw = 2900
        self.doorh = 100
        self.door = 2900

    def get_bb(self):
        return self.doorw - 10, self.doorh - 10, self.doorw + 7, self.doorh + 10

    def update(self):
        if collision.collide(self, server.mario):
            if self.door == 2900:
                game_framework.change_state(main2_state)
        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.doorh -= 2
            else:
                self.doorh += 2

            if server.mario.dir == 1:
                self.doorw -= 7
            else:
                self.doorw += 7

        else:
            self.doorw -= server.mario.dir * 7

    def draw(self):
        self.image.clip_draw(0, 0, 35, 50, self.doorw, self.doorh)
        draw_rectangle(*self.get_bb())