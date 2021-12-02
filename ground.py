from pico2d import *
import server

class Ground:
    def __init__(self):
        self.ground = load_image('ground.png')
        self.groundw = 400
        self.groundh = 350

    def draw(self):
        self.ground.draw(self.groundw, self.groundh)

    def update(self):
        if server.mario.Jump == 1:
            if server.mario.dir == 1:
                self.groundw -= 7
                if server.mario.x < server.mario.x2:
                    self.groundh -= 2
                else:
                    self.groundh += 2

            else:
                self.groundw += 7
                if server.mario.x < server.mario.x2:
                    self.groundh += 2
                else:
                    self.groundh -= 2
        else:
            pass
            # self.groundw -= server.mario.dir * 7