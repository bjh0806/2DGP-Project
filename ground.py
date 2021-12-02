from pico2d import *
import server
import collision

class Ground:
    def __init__(self):
        self.ground = load_image('ground.png')
        self.groundw = 400
        self.groundh = 350

    def get_bb(self):
        return 0, self.groundh - 350, 800, self.groundh - 280

    def draw(self):
        self.ground.draw(self.groundw, self.groundh)
        draw_rectangle(*self.get_bb())

    def update(self):
        if collision.collide(self, server.mario):
            server.mario.JumpStop()

        if server.mario.Jump == 1:
            if server.mario.dir == 1:
                self.groundw -= 7
                if server.mario.Jcount < 10:
                    self.groundh -= 2
                else:
                    self.groundh += 2

            else:
                self.groundw += 7
                if server.mario.Jcount < 10:
                    self.groundh += 2
                else:
                    self.groundh -= 2
        else:
            self.groundw -= server.mario.dir * 7