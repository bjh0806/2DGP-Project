from pico2d import *

class Sky:
    def __init__(self):
        self.sky = load_image('sky.png')
        self.skyw = 400
        self.skyh = 300
        self.Jump = 0
        self.right = 0
        self.left = 0
        self.x = 0
        self.x2 = 0
        self.dir = 0

    def draw(self):
        self.sky.draw(self.skyw, self.skyh)

    def update(self):
        if self.Jump == 1:
            if self.right == 1:
                self.skyw -= 5 // 2
                if self.x < self.x2:
                    self.skyh -= 2
                else:
                    self.skyh += 2

            elif self.left == 1:
                self.skyw += 5 // 2
                if self.x < self.x2:
                    self.skyh += 2
                else:
                    self.skyh -= 2

        else:
            self.skyw -= self.dir * 5 // 2