from pico2d import *

WIDTH, HEIGHT = 1600, 900
left, right = 0, 1

def handle_events():
    global running, x, dir, left, right
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                dir -= 1
                left = 1
                right = 0
            elif event.key == SDLK_d:
                dir += 1
                left = 0
                right = 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                dir += 1
            elif event.key == SDLK_d:
                dir -= 1

open_canvas(WIDTH // 2, 600)

sky = load_image('sky.png')
ground = load_image('ground.png')
mario = load_image('mario.png')

running = True
x = 0
frame = 0
dir = 0

while running:
    clear_canvas()
    sky.draw_now(WIDTH // 4, 200)
    ground.draw_now(WIDTH // 4, 350)
    if right == 1:
        mario.clip_draw(frame * 50, 50, 50, 50, x, 100)
    elif left == 1:
        mario.clip_draw((7 - frame) * 50, 0, 50, 50, x, 95)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x += dir * 5

    delay(0.05)

close_canvas()