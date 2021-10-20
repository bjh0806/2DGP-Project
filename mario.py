from pico2d import *

WIDTH, HEIGHT = 1600, 900

open_canvas(WIDTH // 2, 600)

sky = load_image('sky.png')
ground = load_image('ground.png')
mario = load_image('mario.png')

x = 0
frame = 0

while x < WIDTH:
    clear_canvas()
    sky.draw_now(WIDTH // 4, 200)
    ground.draw_now(WIDTH // 4, 350)
    mario.clip_draw(frame * 50, 0, 50, 50, x, 100)
    update_canvas()
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)

close_canvas()