from pico2d import *

class Ground:
    def __init__(self):
        self.ground = load_image('ground.png')
        self.groundw = 400
        self.groundh = 350
        self.Jump = 0
        self.right = 1
        self.left = 0
        self.x = 0
        self.x2 = 0
        self.dir = 0

    def draw(self):
        self.ground.draw(self.groundw, self.groundh)

    def update(self):
        if self.Jump == 1:
            if self.right == 1:
                self.groundw -= 7
                if self.x < self.x2:
                    self.groundh -= 2
                else:
                    self.groundh += 2

            elif self.left == 1:
                self.groundw += 7
                if self.x < self.x2:
                    self.groundh += 2
                else:
                    self.groundh -= 2
        
        else:
            self.groundw -= self.dir * 7