from pico2d import *
import server

class Ground:
    def __init__(self):
        self.ground = load_image('ground.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.ground.w
        self.h = self.ground.h

    def draw(self):
        self.ground.clip_draw_to_origin(self.window_left, self.window_bottom, server.ground.canvas_width, server.ground.canvas_height, 0, 0)

    def update(self):
        self.window_left = clamp(0, int(server.mario.x) - server.ground.canvas_width // 2, server.ground.w - server.ground.canvas_width)
        self.window_bottom = clamp(100, int(server.mario.y) - server.ground.canvas_height // 2, server.ground.h - server.ground.canvas_height)
        # if server.mario.Jump == 1:
        #     if server.mario.dir == 1:
        #         self.groundw -= 7
        #         if server.mario.x < server.mario.x2:
        #             self.groundh -= 2
        #         else:
        #             self.groundh += 2
        # 
        #     else:
        #         self.groundw += 7
        #         if server.mario.x < server.mario.x2:
        #             self.groundh += 2
        #         else:
        #             self.groundh -= 2
        # else:
        #     pass
        #     # self.groundw -= server.mario.dir * 7