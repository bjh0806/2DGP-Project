from pico2d import *
import random
import game_framework
import server
import collision
import game_world
import main_state

class Door:
    image = None
    def __init__(self):
        if Door.image == None:
            Door.image = load_image('door.png')
        if server.stage == 1:
            self.doorw = 2900
        if server.stage == 2:
            self.doorw = 3700
        if server.stage == 3:
            self.doorw = 3300
        if server.stage == 4:
            self.doorw = 3700
        self.doorh = 100
        self.door = self.doorw
        server.door_sound = load_wav('door_sound.wav')
        server.door_sound.set_volume(64)

    def get_bb(self):
        return self.doorw - 10, self.doorh - 10, self.doorw + 7, self.doorh + 10

    def update(self):
        if collision.collide(self, server.mario):
            if server.stage == 1:
                server.stage = 2
            elif server.stage == 2:
                server.stage = 3
            elif server.stage == 3:
                server.stage = 4
            server.door_sound.play()
            game_world.clear()
            game_framework.change_state(main_state)
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