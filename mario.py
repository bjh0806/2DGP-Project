from pico2d import *
import random
import game_framework
import start_state

name = "MainState"

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, WAIT, JUMP = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

class StartState:
    def enter(Mario, event):
        Mario.Start = 1

    def exit(Mario, event):
        Mario.Start = 0

    def do(Mario):
        global x, Start, Wait
        Mario.firstframe = (Mario.firstframe + 1) % 10
        x += 7
        if Mario.firstframe == 9:
            Mario.Start = 0
            Mario.firstframe = 0
            Mario.add_event(WAIT)

    def draw(Mario):
        if Mario.Start == 1:
            Mario.start.clip_draw(Mario.firstframe * 50, 0, 50, 50, x, y)

class WaitState:
    def enter(Mario, event):
        global Wait, dir
        Wait = 1
        if event == RIGHT_UP:
            dir -= 1
            Wait = 1
        elif event == LEFT_UP:
            dir += 1
            Wait = 1

    def exit(Mario, event):
        global Wait
        Wait = 0

    def do(Mario):
        if Wait == 1:
            Mario.waitframe = (Mario.waitframe + 1) % 7

    def draw(Mario):
        if Wait == 1:
            if right == 1:
                if Mario.mode == 0:
                    Mario.wait.clip_draw(Mario.waitframe * 50, 50, 50, 50, x, y)
                # else:
                #     modewait.clip_draw(waitframe * 50, 50, 50, 50, x, y)
            elif left == 1:
                if Mario.mode == 0:
                    Mario.wait.clip_draw(Mario.waitframe * 50, 0, 50, 50, x, y)
                # else:
                #     modewait.clip_draw(waitframe * 50, 0, 50, 50, x, y)

class JumpState:
    def enter(Mario, event):
        global jump
        jump = 1

    def exit(Mario, event):
        pass

    def do(Mario):
        global jump, i, y, y1, y2, y3
        if jump == 1:
            if i == 0:
                y1 = y
                y3 = y
                y2 = y + 75

            t = i / 100

            y = (2 * t ** 2 - 3 * t + 1) * y1 + (-4 * t ** 2 + 4 * t) * y2 + (2 * t ** 2 - t) * y3

            i += 4

            if i == 104:
                jump = 0
                i = 0
                Mario.add_event(WAIT)

            Mario.jumpframe = (Mario.jumpframe + 1) % 14

    def draw(Mario):
        if jump == 1:
            if right == 1:
                if Mario.mode == 0:
                    Mario.jump.clip_draw((Mario.jumpframe + 5) * 50, 50, 50, 50, x, y)
                # else:
                #     modejump.clip_draw(jumpframe * 50, 50, 50, 50, x, y)
            elif left == 1:
                if Mario.mode == 0:
                    Mario.jump.clip_draw((13 - Mario.jumpframe) * 50, 0, 50, 50, x, y)
                # else:
                #     modejump.clip_draw((13 - jumpframe) * 50, 0, 50, 50, x, y)

class MjumpState:
    def enter(Mario, event):
        global Jump
        Jump = 1

    def exit(Mario, event):
        pass

    def do(Mario):
        global Jump, i, x, y, x1, x2, x3, y1, y2, y3
        if Jump == 1:
            if i == 0:
                if right == 1:
                    x1, y1 = x, y
                    x3, y3 = x + 20, y
                    x2, y2 = x + 10, y + 75
                elif left == 1:
                    x1, y1 = x, y
                    x3, y3 = x - 20, y
                    x2, y2 = x - 10, y + 75

            t = i / 100

            x = (2 * t ** 2 - 3 * t + 1) * x1 + (-4 * t ** 2 + 4 * t) * x2 + (2 * t ** 2 - t) * x3
            y = (2 * t ** 2 - 3 * t + 1) * y1 + (-4 * t ** 2 + 4 * t) * y2 + (2 * t ** 2 - t) * y3

            i += 4

            if i == 104:
                Jump = 0
                i = 0
                Mario.add_event(WAIT)

            Mario.jumpframe = (Mario.jumpframe + 1) % 14

    def draw(Mario):
        if Jump == 1:
            if right == 1:
                if Mario.mode == 0:
                    Mario.jump.clip_draw((Mario.jumpframe + 5) * 50, 50, 50, 50, x, y)
                # else:
                #     modejump.clip_draw(jumpframe * 50, 50, 50, 50, x, y)
            elif left == 1:
                if Mario.mode == 0:
                    Mario.jump.clip_draw((13 - Mario.jumpframe) * 50, 0, 50, 50, x, y)
                # else:
                #     modejump.clip_draw((13 - jumpframe) * 50, 0, 50, 50, x, y)

class WalkState:
    def enter(Mario, event):
        global dir, left, right, Wait
        if event == RIGHT_DOWN:
            dir += 1
            left = 0
            right = 1
            Wait = 0
        elif event == LEFT_DOWN:
            dir -= 1
            left = 1
            right = 0
            Wait = 0

    def exit(Mario, event):
        pass

    def do(Mario):
        global x
        Mario.frame = (Mario.frame + 1) % 8
        if x >= 10 and x <= 250:
            x += dir * 5

    def draw(Mario):
        if right == 1:
            if Mario.mode == 0:
                Mario.mario.clip_draw(Mario.frame * 50, 50, 50, 50, x, y)
            # else:
            #     walk.clip_draw(frame * 50, 50, 50, 50, x, y)
        elif left == 1:
            if Mario.mode == 0:
                Mario.mario.clip_draw((7 - Mario.frame) * 50, 0, 50, 50, x, y - 5)
            # else:
            #     self.walk.clip_draw((7 - self.frame) * 50, 0, 50, 50, self.x, self.y)

next_state_table = {
    StartState: {WAIT: WaitState},
    WaitState: {SPACE: JumpState, RIGHT_DOWN: WalkState,
                LEFT_DOWN: WalkState},
    JumpState: {JUMP: JumpState, WAIT: WaitState},
    WalkState: {RIGHT_DOWN: WalkState, LEFT_DOWN: WalkState,
                RIGHT_UP: WaitState, LEFT_UP: WaitState}
}

WIDTH, HEIGHT = 1600, 900
left, right = 0, 1
last = 1
random_boxw = [300, 400, 425, 855, 1100, 1900, 2025]
random_boxh = [200, 200, 200, 300, 200, 200, 200]
upgroundw = [700]
upgroundh = 50
upground2w = [850]
upground2h = 70
coinw = [580, 610, 640, 740, 770, 800]
coinh = [130, 160, 180, 180, 210, 230]
skyw = WIDTH // 4
skyh = 300
groundw = WIDTH // 4
groundh = 350
x = 0
y = 95
dir = 0
Wait = 0
Jump = 0
jump = 0
i = 0
x1 = 0
x2 = 0
x3 = 0
y1 = 0
y2 = 0
y3 = 0

class Sky:
    def __init__(self):
        self.sky = load_image('sky.png')

    def draw(self):
        self.sky.draw(skyw, skyh)

    def update(self):
        global skyh, skyw

        if Jump == 1:
            if right == 1:
                skyw -= 5 // 2
                if x < x2:
                    skyh -= 2
                else:
                    skyh += 2

            elif left == 1:
                skyw += 5 // 2
                if x < x2:
                    skyh += 2
                else:
                    skyh -= 2

        else:
            skyw -= dir * 5 // 2

class Ground:
    def __init__(self):
        self.ground = load_image('ground.png')

    def draw(self):
        self.ground.draw(groundw, groundh)

    def update(self):
        global groundh, groundw

        if Jump == 1:
            if right == 1:
                groundw -= 7
                if x < x2:
                    groundh -= 2
                else:
                    groundh += 2

            elif left == 1:
                groundw += 7
                if x < x2:
                    groundh += 2
                else:
                    groundh -= 2

        else:
            groundw -= dir * 7

class Mario:
    def __init__(self):
        self.Start = 1
        self.mode = 0
        self.i = 0
        self.firstframe = 0
        self.waitframe = 0
        self.frame = 0
        self.jumpframe = 0
        self.start = load_image('start.png')
        self.wait = load_image('wait.png')
        self.mario = load_image('mario.png')
        self.jump = load_image('jump.png')
        self.event_que = []
        if self.Start == 1:
            self.cur_state = StartState
        else:
            self.cur_state = WaitState
        self.cur_state.enter(self, None)

    def change_state(self, state):
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        # global x, y, Wait, skyw, groundw, i, skyh, groundh, upgroundh, upground2h, Jump, x1, x2, x3, y1, y2, y3
        #
        # else:
        #     self.frame = (self.frame + 1) % 8
        #     if x >= 10 and x <= 250:
        #         x += dir * 5

    def draw(self):
        self.cur_state.draw(self)
        debug_print('State: ' + str(self.cur_state))
        # global Wait, Jump, skyh, groundh, upgroundh, upground2h, i
        #
        # elif right == 1:
        #     if self.mode == 0:
        #         self.mario.clip_draw(self.frame * 50, 50, 50, 50, x, y)
        #     # else:
        #     #     walk.clip_draw(frame * 50, 50, 50, 50, x, y)
        # elif left == 1:
        #     if self.mode == 0:
        #         self.mario.clip_draw((7 - self.frame) * 50, 0, 50, 50, x, y - 5)
        #     # else:
        #     #     self.walk.clip_draw((7 - self.frame) * 50, 0, 50, 50, self.x, self.y)

class Object:
    upground = None
    upground2 = None
    random_box = None
    coin = None

    def __init__(self):
        if Object.random_box == None:
            Object.random_box = load_image('random_box.png')
        if Object.upground == None:
            Object.upground = load_image('upground.png')
        if Object.upground2 == None:
            Object.upground2 = load_image('upground_double.png')
        if Object.coin == None:
            Object.coin = load_image('coin.png')
        self.randomframe = random.randint(0, 3)

    def update_random_box(self):
        self.randomframe = (self.randomframe + 1) % 4

    def update(self):
        global upgroundh, upground2h

        if Jump == 1:
            if right == 1:
                for j in range(0, len(random_boxw)):
                    random_boxw[j] -= 7
                for k in range(0, len(upgroundw)):
                    upgroundw[k] -= 7
                for l in range(0, len(upground2w)):
                    upground2w[l] -= 7
                for m in range(0, len(coinw)):
                    coinw[m] -= 7
                if x < x2:
                    for j in range(0, len(random_boxh)):
                        random_boxh[j] -= 2
                    for m in range(0, len(coinh)):
                        coinh[m] -= 2
                    upgroundh -= 2
                    upground2h -= 2
                else:
                    for j in range(0, len(random_boxh)):
                        random_boxh[j] += 2
                    for m in range(0, len(coinh)):
                        coinh[m] += 2
                    upgroundh += 2
                    upground2h += 2

            elif left == 1:
                for j in range(0, len(random_boxw)):
                    random_boxw[j] += 7
                for k in range(0, len(upgroundw)):
                    upgroundw[k] += 7
                for l in range(0, len(upground2w)):
                    upground2w[l] += 7
                for m in range(0, len(coinw)):
                    coinw[m] += 7
                if x < x2:
                    for j in range(0, len(random_boxh)):
                        random_boxh[j] += 2
                    for m in range(0, len(coinh)):
                        coinh[m] += 2
                    upgroundh += 2
                    upground2h += 2
                else:
                    for j in range(0, len(random_boxh)):
                        random_boxh[j] -= 2
                    for m in range(0, len(coinh)):
                        coinh[m] -= 2
                    upgroundh -= 2
                    upground2h -= 2

        else:
            for j in range(0, len(random_boxw)):
                random_boxw[j] -= dir * 7
            for k in range(0, len(upgroundw)):
                upgroundw[k] -= dir * 7
            for l in range(0, len(upground2w)):
                upground2w[l] -= dir * 7
            for m in range(0, len(coinw)):
                coinw[m] -= dir * 7

    def draw_random_box(self):
        for j in range(0, len(random_boxw)):
            self.random_box.clip_draw(self.randomframe * 25, 0, 25, 33, random_boxw[j], random_boxh[j])

    def draw_upground(self):
        for k in range(0, len(upgroundw)):
            self.upground.draw(upgroundw[k], upgroundh)

    def draw_upground2(self):
        for l in range(0, len(upground2w)):
            self.upground2.draw(upground2w[l], upground2h)

    def draw_coin(self):
        for m in range(0, len(coinw)):
            self.coin.draw(coinw[m], coinh[m])

def enter():
    global object, sky, ground, mario
    object = Object()
    sky = Sky()
    ground = Ground()
    mario = Mario()

def exit():
    global object, sky, ground, mario
    del(object)
    del(sky)
    del(ground)
    del(mario)

def handle_events():
    global x, dir, left, right, Wait, Jump, Attack1, Attack3, keep
    events = get_events()
    for event in events:
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            mario.add_event(key_event)
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            # if event.key == SDLK_a:
            #     dir -= 1
            #     left = 1
            #     right = 0
            #     Wait = 0
            # elif event.key == SDLK_d:
            #     dir += 1
            #     left = 0
            #     right = 1
            #     Wait = 0
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(start_state)
        #     elif event.key == SDLK_SPACE:
        #         Jump = 1
        #         Wait = 0
        #     elif event.key == SDLK_z:
        #         Attack1 = 1
        #         Wait = 0
        #     elif event.key == SDLK_LCTRL:
        #         if mode == 1:
        #             Attack3 = 1
        #             keep = 1
        #             Wait = 0
        # elif event.type == SDL_KEYUP:
        #     if event.key == SDLK_a:
        #         dir += 1
        #         if Jump == 0:
        #             Wait = 1
        #     elif event.key == SDLK_d:
        #         dir -= 1
        #         if Jump == 0:
        #             Wait = 1

def update():
    handle_events()
    object.update_random_box()
    mario.update()
    sky.update()
    ground.update()
    object.update()
    delay(0.05)

def draw():
    clear_canvas()
    sky.draw()
    ground.draw()
    mario.draw()
    object.draw_random_box()
    object.draw_upground()
    object.draw_upground2()
    object.draw_coin()
    update_canvas()

# open_canvas(WIDTH // 2, 600)
#
# attack1 = load_image('attack1.png')
# flower = load_image('flower.png')
# strong = load_image('strong.png')
# modewait = load_image('modewait.png')
# walk = load_image('walk.png')
# modejump = load_image('modejump.png')
# attack2 = load_image('attack2.png')
# attack3 = load_image('attack3.png')
# fire = load_image('fire.png')
#
# Attack1 = 0
# attackframe1 = 0
# getflower = 0
# Get = 0
# use = 0
# fireframe = 0
# mode = 0
# attackframe2 = 0
# Attack3 = 0
# attackframe3 = 0
# longattack = 0
# keep = 0
# firex = 50
# firey = 100
#
#
#
# while running:
#     clear_canvas()
#
#     elif Attack1 == 1:
#         if right == 1:
#             if mode == 0:
#                 attack1.clip_draw(attackframe1 * 50, 50, 50, 50, x, y)
#             else:
#                 if i == 0:
#                     if right == 1:
#                         x1, y1 = x, y
#                         x3, y3 = x + 10, y
#                         x2, y2 = x + 5, y + 20
#                     elif left == 1:
#                         x1, y1 = x, y
#                         x3, y3 = x + 10, y
#                         x2, y2 = x + 5, y + 20
#
#                 t = i / 100
#                 x = (2 * t ** 2 - 3 * t + 1) * x1 + (-4 * t ** 2 + 4 * t) * x2 + (2 * t ** 2 - t) * x3
#                 y = (2 * t ** 2 - 3 * t + 1) * y1 + (-4 * t ** 2 + 4 * t) * y2 + (2 * t ** 2 - t) * y3
#
#                 i += 10
#
#                 attack2.clip_draw(attackframe2 * 50, 60, 50, 60, x, y)
#
#                 if i == 110:
#                     Attack1 = 0
#                     Wait = 1
#                     i = 0
#
#         elif left == 1:
#             if mode == 0:
#                 attack1.clip_draw((10 - attackframe1) * 50, 0, 50, 50, x, y)
#             else:
#                 attack2.clip_draw((7 - attackframe2) * 50, 0, 50, 60, x, y)
#
#     elif Attack3 == 1:
#         if right == 1:
#             attack3.clip_draw(attackframe3 * 50, 50, 50, 50, x, y)
#             last = 1
#         elif left == 1:
#             attack3.clip_draw((7 - attackframe3) * 50, 0, 50, 50, x, y)
#             last = 0
#
#     elif Get == 1:
#         if right == 1:
#             strong.clip_draw(fireframe * 50, 100, 50, 100, x, y + 27)
#         elif left == 1:
#             strong.clip_draw((16 - fireframe) * 50, 0, 50, 100, x, y + 27)
#
#     if keep == 1:
#         if last == 1:
#             fire.clip_draw(longattack * 70, 50, 70, 50, x + firex, firey)
#         elif last == 0:
#             fire.clip_draw((1 - longattack) * 70, 0, 70, 50, x - firex, firey)
#         firex += 5
#
#     update_canvas()
#
#     handle_events()
#
#     elif Attack1 == 1:
#         if mode == 0:
#             attackframe1 = (attackframe1 + 1) % 11
#         else:
#             attackframe2 = (attackframe2 + 1) % 8
#     elif mode == 1 and Attack3 == 1:
#         attackframe3 = (attackframe3 + 1) % 8
#     elif Get == 1:
#         fireframe = (fireframe + 1) % 17
#
#     if keep == 1:
#         longattack = (longattack + 1) % 2
#
#
#     if attackframe1 == 10:
#         Attack1 = 0
#         Wait = 1
#         attackframe1 = 0
#
#     if attackframe3 == 7:
#         Attack3 = 0
#         Wait = 1
#         attackframe3 = 0
#
#     if fireframe == 16:
#         Get = 0
#         Wait = 1
#         fireframe = 0
#         mode = 1
#
#     if left == 0 and right == 0:
#         Wait = 1
#
#
# close_canvas()