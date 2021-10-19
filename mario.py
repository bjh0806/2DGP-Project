from pico2d import *

WIDTH, HEIGHT = 1600, 900

open_canvas(WIDTH, HEIGHT)

sky = load_image('sky.png')
ground = load_image('ground.png')

sky.draw_now(WIDTH // 2, HEIGHT // 2)
ground.draw_now(WIDTH // 2, HEIGHT // 2)

delay(5)

close_canvas()