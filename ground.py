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
        if server.Mario.Jump == 1:
            if server.Mario.dir == 1:
                self.groundw -= 7
                if server.Mario.x < server.Mario.x2:
                    self.groundh -= 2
                else:
                    self.groundh += 2

            else:
                self.groundw += 7
                if server.Mario.x < server.Mario.x2:
                    self.groundh += 2
                else:
                    self.groundh -= 2
        else:
            self.groundw -= server.Mario.dir * 7