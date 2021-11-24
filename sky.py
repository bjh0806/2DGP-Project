from pico2d import *

class Sky:
    dir = 0
    Jump = 0
    x = 0
    x2 = 0
    def __init__(self):
        self.sky = load_image('sky.png')
        self.skyw = 400
        self.skyh = 300
        
    def draw(self):
        self.sky.draw(self.skyw, self.skyh)
        
    def update(self):
        if Sky.Jump == 1:
            if Sky.dir == 1:
                self.skyw -= 5 // 2
                if Sky.x < Sky.x2:
                    self.skyh -= 2
                else:
                    self.skyh += 2
            else:
                self.skyw += 5 // 2
                if Sky.x < Sky.x2:
                    self.skyh += 2
                else:
                    self.skyh -= 2
        else:
            self.skyw -= Sky.dir * 5 // 2