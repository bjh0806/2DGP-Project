from pico2d import *
import server
import collision

class Sky:
    def __init__(self):
        self.sky = load_image('sky.png')
        self.skyw = 400
        self.skyh = 200
        
    def draw(self):
        self.sky.draw(self.skyw, self.skyh)
        
    def update(self):
        if server.mario.Jump == 1:
            if server.mario.dir == 1:
                self.skyw -= 5 // 2
                if server.mario.Jcount < 10:
                    self.skyh -= 2
                else:
                    self.skyh += 2
            else:
                self.skyw += 5 // 2
                if server.mario.Jcount < 10:
                    self.skyh += 2
                else:
                    self.skyh -= 2
        else:
            self.skyw -= server.mario.dir * 5 // 2