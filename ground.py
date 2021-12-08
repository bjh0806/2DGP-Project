from pico2d import *
import server
import collision

class Ground:
    def __init__(self):
        self.ground = load_image('ground.png')
        if server.stage == 1 or server.stage == 4:
            self.back = load_image('back1.png')
            self.backh = 450
        if server.stage == 2:
            self.back = load_image('back2.png')
            self.backh = 500
        if server.stage == 3:
            self.back = load_image('back3.png')
            self.backh = 450
        self.groundw = 400
        self.groundh = 350
        self.backw = 1200

    def get_bb(self):
        return 0, self.groundh - 350, 800, self.groundh - 280

    def draw(self):
        self.back.draw(self.backw, self.backh)
        self.ground.draw(self.groundw, self.groundh)

    def update(self):
        if collision.collide(self, server.mario):
            server.mario.JumpStop()

        if server.mario.Jump == 1:
            if server.mario.Jcount < 10:
                self.groundh -= 2
                self.backh -= 2
            else:
                self.groundh += 2
                self.backh += 2

            if server.mario.dir == 1:
                self.groundw -= 7
                self.backw -= 7
            else:
                self.groundw += 7
                self.backw += 7

        else:
            self.groundw -= server.mario.dir * 7
            self.backw -= server.mario.dir * 7