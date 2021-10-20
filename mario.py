from pico2d import *

WIDTH, HEIGHT = 1600, 900
left, right = 0, 1

def handle_events():
    global running, x, dir, left, right, Wait, Jump, Attack1
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                dir -= 1
                left = 1
                right = 0
                Wait = 0
            elif event.key == SDLK_d:
                dir += 1
                left = 0
                right = 1
                Wait = 0
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_SPACE:
                Jump = 1
                Wait = 0
            elif event.key == SDLK_z:
                Attack1 = 1
                Wait = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                dir += 1
                if Jump == 0:
                    Wait = 1
            elif event.key == SDLK_d:
                dir -= 1
                if Jump == 0:
                    Wait = 1

open_canvas(WIDTH // 2, 600)

sky = load_image('sky.png')
ground = load_image('ground.png')
mario = load_image('mario.png')
start = load_image('start.png')
wait = load_image('wait.png')
jump = load_image('jump.png')
attack1 = load_image('attack1.png')

running = True
x = 0
y = 100
frame = 0
dir = 0
Start = 1
firstframe = 0
Wait = 0
waitframe = 0
Jump = 0
i = 0
jumpframe = 0
Attack1 = 0
attackframe1 = 0

skyw = WIDTH // 4
skyh = 200
groundw = WIDTH // 4
groundh = 350

while running:
    clear_canvas()
    sky.draw_now(skyw, skyh)
    ground.draw_now(groundw, groundh)
    if Start == 1:
        start.clip_draw(firstframe * 50, 0, 50, 50, x, y)
    elif Wait == 1:
        if right == 1:
            wait.clip_draw(waitframe * 50, 50, 50, 50, x, y)
        elif left == 1:
            wait.clip_draw(waitframe * 50, 0, 50, 50, x, y)
    elif Jump == 1:
        if i == 0:
            if right == 1:
                x1, y1 = x, y
                x3, y3 = x + 150, y
                x2, y2 = x + 75, y + 75
            elif left == 1:
                x1, y1 = x, y
                x3, y3 = x - 150, y
                x2, y2 = x - 75, y + 75

        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * x1 + (-4 * t ** 2 + 4 * t) * x2 + (2 * t ** 2 - t) * x3
        y = (2 * t ** 2 - 3 * t + 1) * y1 + (-4 * t ** 2 + 4 * t) * y2 + (2 * t ** 2 - t) * y3

        if right == 1:
            if x < x2:
                skyh -= 2
                groundh -= 2
            else:
                skyh += 2
                groundh += 2
        elif left == 1:
            if x < x2:
                skyh += 2
                groundh += 2
            else:
                skyh -= 2
                groundh -= 2

        i += 4

        if right == 1:
            jump.clip_draw((jumpframe + 5) * 50, 50, 50, 50, x, y)
        elif left == 1:
            jump.clip_draw((13 - jumpframe) * 50, 0, 50, 50, x, y)

        if i == 104:
            Jump = 0
            Wait = 1
            i = 0

    elif Attack1 == 1:
        if right == 1:
            attack1.clip_draw(attackframe1 * 50, 50, 50, 50, x, y)
        elif left == 1:
            attack1.clip_draw((10 - attackframe1) * 50, 0, 50, 50, x, y)

    elif right == 1:
        mario.clip_draw(frame * 50, 50, 50, 50, x, y)
    elif left == 1:
        mario.clip_draw((7 - frame) * 50, 0, 50, 50, x, y - 5)

    update_canvas()

    handle_events()

    if Start == 1:
        firstframe = (firstframe + 1) % 10
        x += 7
    elif Wait == 1:
        waitframe = (waitframe + 1) % 7
    elif Jump == 1:
        jumpframe = (jumpframe + 1) % 14
        if right == 1:
            skyw -= 5 // 2
            groundw -= 7
        elif left == 1:
            skyw += 5 // 2
            groundw += 7
    elif Attack1 == 1:
        attackframe1 = (attackframe1 + 1) % 11
        if right == 1:
            x += 3
            skyw -= 1
            groundw -= 2
        elif left == 1:
            x -= 3
            skyw += 1
            groundw += 2
    else:
        frame = (frame + 1) % 8
        x += dir * 5
        skyw -= dir * 5 // 2
        groundw -= dir * 7

    if firstframe == 9:
        Start = 0
        Wait = 1
        firstframe = 0

    if attackframe1 == 10:
        Attack1 = 0

    if left == 0 and right == 0:
        Wait = 1

    delay(0.05)

close_canvas()