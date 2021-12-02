from pico2d import *
import server
import collision

class Sky:
    def __init__(self):
        self.sky = load_image('sky.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.sky.w
        self.h = self.sky.h
        
    def draw(self):
        self.sky.clip_draw_to_origin(self.window_left, self.window_bottom, server.sky.canvas_width, server.sky.canvas_height, 0, 0)
        
    def update(self):
        self.window_left = clamp(0, int(server.mario.x) - server.sky.canvas_width // 2, server.sky.w - server.sky.canvas_width)
        self.window_bottom = clamp(150, int(server.mario.y) - server.sky.canvas_height // 2, server.sky.h - server.sky.canvas_height)
        # if server.mario.Jump == 1:
        #     if server.mario.dir == 1:
        #         self.skyw -= 5 // 2
        #         if server.mario.x < server.mario.x2:
        #             self.skyh -= 2
        #         else:
        #             self.skyh += 2
        #     else:
        #         self.skyw += 5 // 2
        #         if server.mario.x < server.mario.x2:
        #             self.skyh += 2
        #         else:
        #             self.skyh -= 2
        # else:
        #     pass
        #     # self.skyw -= server.mario.dir * 5 // 2