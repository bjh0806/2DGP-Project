from pico2d import *

class Ground:
    dir = 0
    Jump = 0
    x = 0
    x2 = 0
    def __init__(self):
        self.ground = load_image('ground.png')
        self.groundw = 400
        self.groundh = 350

    def draw(self):
        self.ground.draw(self.groundw, self.groundh)

    def update(self):
        if Ground.Jump == 1:
            if Ground.dir == 1:
                self.groundw -= 7
                if Ground.x < Ground.x2:
                    self.groundh -= 2
                else:
                    self.groundh += 2

            else:
                self.groundw += 7
                if Ground.x < Ground.x2:
                    self.groundh += 2
                else:
                    self.groundh -= 2
        else:
            self.groundw -= Ground.dir * 0.7