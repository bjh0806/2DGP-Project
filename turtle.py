import random
from pico2d import *
import game_world
import game_framework
import server
import collision

class Turtle:
    image = None
    kill_image = None
    def __init__(self, x = 450, y = 95):
        if Turtle.image == None:
            Turtle.image = load_image('turtle.png')
        if Turtle.kill_image == None:
            Turtle.kill_image = load_image('turtle_kill.png')
        self.turtlex, self.turtley = x, y
        self.frame = random.randint(0, 9)
        self.look = random.randint(0, 1)
        self.moveg = 0
        self.kill = 0
        server.goomba_sound = load_wav('goomba_sound.wav')
        server.goomba_sound.set_volume(64)

    def get_bb(self):
        return self.turtlex - 12, self.turtley - 11, self.turtlex + 11, self.turtley + 11

    def update(self):
        self.frame = (self.frame + 10 * game_framework.frame_time) % 10
        if collision.collide(self, server.mario):
            if self.kill == 0:
                server.goomba_sound.play()
            self.kill = 1
        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.turtley -= 2
            else:
                self.turtley += 2

            if server.mario.dir == 1:
                self.turtlex -= 7

            else:
                self.turtlex += 7

            if self.kill == 0:
                if self.look == 0:
                    self.moveg -= 2
                    self.turtlex -= 2

                elif self.look == 1:
                    self.moveg += 2
                    self.turtlex += 2

        else:
            self.turtlex -= server.mario.dir * 7

            if self.kill == 0:
                if self.look == 0:
                    self.moveg -= 2
                    self.turtlex -= 2

                elif self.look == 1:
                    self.moveg += 2
                    self.turtlex += 2

        if self.moveg <= -50:
            self.look = 1
            self.moveg = 0
        elif self.moveg >= 50:
            self.look = 0
            self.moveg = 0

    def draw(self):
        if self.kill == 0:
            if self.look == 0:
                self.image.clip_draw(int(self.frame) * 25, 40, 25, 40, self.turtlex, self.turtley)
            else:
                self.image.clip_draw((9 - int(self.frame)) * 25, 0, 25, 40, self.turtlex, self.turtley)
        else:
            self.kill_image.draw(self.turtlex, self.turtley - 3)