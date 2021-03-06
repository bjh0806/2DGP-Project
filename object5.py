from pico2d import *
import random
import game_framework
import server
import collision

class Object5:
    block = None
    def __init__(self, w = 1075, h = 200):
        if Object5.block == None:
            Object5.block = load_image('block.png')
        self.frame = random.randint(0, 3)
        self.blockw = w
        self.blockh = h
        server.block_sound = load_wav('block_sound.wav')
        server.block_sound.set_volume(64)

    def get_bb(self):
        return self.blockw - 15, self.blockh - 16.5, self.blockw + 14, self.blockh + 10

    def update(self):
        self.frame = (self.frame + 8 * game_framework.frame_time) % 4
        if collision.collide(self, server.mario):
            if server.mario.Jump == 1:
                server.block_sound.play()
                server.mario.JumpStop()

        if server.stage != 5:
            if server.mario.Jump == 1:
                if server.mario.Jcount < 10:
                    self.blockh -= 2
                else:
                    self.blockh += 2

                if server.mario.dir == 1:
                    self.blockw -= 7
                else:
                    self.blockw += 7

            else:
                self.blockw -= server.mario.dir * 7

    def draw(self):
        self.block.clip_draw(int(self.frame) * 25, 0, 25, 33, self.blockw, self.blockh)