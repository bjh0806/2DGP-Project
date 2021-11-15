from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, WAIT = range(6)

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
        global Jump, dir
        Jump = 1
        if event == RIGHT_UP:
            dir -= 1
        elif event == LEFT_UP:
            dir += 1

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
    StartState: {WAIT: WaitState, RIGHT_DOWN: StartState,
                 LEFT_DOWN: StartState, RIGHT_UP: StartState,
                 LEFT_UP: StartState},
    WaitState: {SPACE: JumpState, RIGHT_DOWN: WalkState,
                LEFT_DOWN: WalkState, RIGHT_UP: WaitState,
                LEFT_UP: WaitState},
    JumpState: {WAIT: WaitState},
    WalkState: {RIGHT_DOWN: WalkState, LEFT_DOWN: WalkState,
                RIGHT_UP: WaitState, LEFT_UP: WaitState,
                SPACE: MjumpState},
    MjumpState: {WAIT: WaitState, RIGHT_DOWN: WalkState,
                 LEFT_DOWN: WalkState, RIGHT_UP: MjumpState,
                 LEFT_UP: MjumpState}
}

left, right = 0, 1
last = 1
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

    def draw(self):
        self.cur_state.draw(self)
        debug_print('State: ' + str(self.cur_state))

    def handle_event(self, event):
        global x, dir, left, right, Wait, Jump, Attack1, Attack3, keep
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

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