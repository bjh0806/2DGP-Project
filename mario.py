from pico2d import *
import game_framework
from ground import Ground
from sky import Sky
from object import Object
from object2 import Object2
from object3 import Object3
from object4 import Object4
from object5 import Object5
from goomba import Goomba

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

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
        Mario.firstframe = (Mario.firstframe + 1) % 10
        Mario.x += 7
        Ground.x = Mario.x
        Sky.x = Mario.x
        Object.x = Mario.x
        Object2.x = Mario.x
        Object3.x = Mario.x
        Object4.x = Mario.x
        Object5.x = Mario.x
        Goomba.x = Mario.x
        if Mario.firstframe == 9:
            Mario.Start = 0
            Mario.firstframe = 0
            Mario.add_event(WAIT)

    def draw(Mario):
        if Mario.Start == 1:
            Mario.start.clip_draw(Mario.firstframe * 50, 0, 50, 50, Mario.x, Mario.y)

class WaitState:
    def enter(Mario, event):
        Mario.Wait = 1

    def exit(Mario, event):
        Mario.Wait = 0

    def do(Mario):
        if Mario.Wait == 1:
            Mario.waitframe = (Mario.waitframe + 7 * ACTION_PER_TIME * game_framework.frame_time) % 7

    def draw(Mario):
        if Mario.Wait == 1:
            if Mario.right == 1:
                if Mario.mode == 0:
                    Mario.wait.clip_draw(int(Mario.waitframe) * 50, 50, 50, 50, Mario.x, Mario.y)
                # else:
                #     modewait.clip_draw(waitframe * 50, 50, 50, 50, x, y)
            elif Mario.left == 1:
                if Mario.mode == 0:
                    Mario.wait.clip_draw(int(Mario.waitframe) * 50, 0, 50, 50, Mario.x, Mario.y)
                # else:
                #     modewait.clip_draw(waitframe * 50, 0, 50, 50, x, y)

class JumpState:
    def enter(Mario, event):
        Mario.jj = 1

    def exit(Mario, event):
        pass

    def do(Mario):
        if Mario.jj == 1:
            if Mario.i == 0:
                Mario.y1 = Mario.y
                Mario.y3 = Mario.y
                Mario.y2 = Mario.y + 75

            t = Mario.i / 100

            Mario.y = (2 * t ** 2 - 3 * t + 1) * Mario.y1 + (-4 * t ** 2 + 4 * t) * Mario.y2 + (2 * t ** 2 - t) * Mario.y3

            Mario.i += 4

            if Mario.i == 104:
                Mario.jj = 0
                Mario.i = 0
                Mario.add_event(WAIT)

            Mario.jumpframe = (Mario.jumpframe + 14 * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(Mario):
        if Mario.jj == 1:
            if Mario.right == 1:
                if Mario.mode == 0:
                    Mario.jump.clip_draw((int(Mario.jumpframe) + 5) * 50, 50, 50, 50, Mario.x, Mario.y)
                # else:
                #     modejump.clip_draw(jumpframe * 50, 50, 50, 50, x, y)
            elif Mario.left == 1:
                if Mario.mode == 0:
                    Mario.jump.clip_draw((13 - int(Mario.jumpframe)) * 50, 0, 50, 50, Mario.x, Mario.y)
                # else:
                #     modejump.clip_draw((13 - jumpframe) * 50, 0, 50, 50, x, y)

class MjumpState:
    def enter(Mario, event):
        Mario.Jump = 1
        Ground.Jump = Mario.Jump
        Sky.Jump = Mario.Jump
        Object.Jump = Mario.Jump
        Object2.Jump = Mario.Jump
        Object3.Jump = Mario.Jump
        Object4.Jump = Mario.Jump
        Object5.Jump = Mario.Jump
        Goomba.Jump = Mario.Jump

    def exit(Mario, event):
        pass

    def do(Mario):
        if Mario.Jump == 1:
            if Mario.i == 0:
                if Mario.right == 1:
                    Mario.x1, Mario.y1 = Mario.x, Mario.y
                    Mario.x3, Mario.y3 = Mario.x + 20, Mario.y
                    Mario.x2, Mario.y2 = Mario.x + 10, Mario.y + 75
                    Ground.x2 = Mario.x2
                    Sky.x2 = Mario.x2
                    Object.x2 = Mario.x2
                    Object2.x2 = Mario.x2
                    Object3.x2 = Mario.x2
                    Object4.x2 = Mario.x2
                    Object5.x2 = Mario.x2
                    Goomba.x2 = Mario.x2
                elif Mario.left == 1:
                    Mario.x1, Mario.y1 = Mario.x, Mario.y
                    Mario.x3, Mario.y3 = Mario.x - 20, Mario.y
                    Mario.x2, Mario.y2 = Mario.x - 10, Mario.y + 75
                    Ground.x2 = Mario.x2
                    Sky.x2 = Mario.x2
                    Object.x2 = Mario.x2
                    Object2.x2 = Mario.x2
                    Object3.x2 = Mario.x2
                    Object4.x2 = Mario.x2
                    Object5.x2 = Mario.x2
                    Goomba.x2 = Mario.x2

            t = Mario.i / 100

            Mario.x = (2 * t ** 2 - 3 * t + 1) * Mario.x1 + (-4 * t ** 2 + 4 * t) * Mario.x2 + (2 * t ** 2 - t) * Mario.x3
            Mario.y = (2 * t ** 2 - 3 * t + 1) * Mario.y1 + (-4 * t ** 2 + 4 * t) * Mario.y2 + (2 * t ** 2 - t) * Mario.y3

            Ground.x = Mario.x
            Sky.x = Mario.x
            Object.x = Mario.x
            Object2.x = Mario.x
            Object3.x = Mario.x
            Object4.x = Mario.x
            Object5.x = Mario.x
            Goomba.x = Mario.x

            Mario.i += 4

            if Mario.i == 104:
                Mario.Jump = 0
                Ground.Jump = Mario.Jump
                Sky.Jump = Mario.Jump
                Object.Jump = Mario.Jump
                Object2.Jump = Mario.Jump
                Object3.Jump = Mario.Jump
                Object4.Jump = Mario.Jump
                Object5.Jump = Mario.Jump
                Goomba.Jump = Mario.Jump
                Mario.i = 0
                Mario.add_event(WAIT)

            Mario.jumpframe = (Mario.jumpframe + 14 * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(Mario):
        if Mario.Jump == 1:
            if Mario.right == 1:
                if Mario.mode == 0:
                    Mario.jump.clip_draw((int(Mario.jumpframe) + 5) * 50, 50, 50, 50, Mario.x, Mario.y)
                # else:
                #     modejump.clip_draw(jumpframe * 50, 50, 50, 50, x, y)
            elif Mario.left == 1:
                if Mario.mode == 0:
                    Mario.jump.clip_draw((13 - int(Mario.jumpframe)) * 50, 0, 50, 50, Mario.x, Mario.y)
                # else:
                #     modejump.clip_draw((13 - jumpframe) * 50, 0, 50, 50, x, y)

class WalkState:
    def enter(Mario, event):
        if event == RIGHT_DOWN:
            Mario.velocity += RUN_SPEED_PPS
            Mario.left = 0
            Ground.left = Mario.left
            Sky.left = Mario.left
            Object.left = Mario.left
            Object2.left = Mario.left
            Object3.left = Mario.left
            Object4.left = Mario.left
            Object5.left = Mario.left
            Goomba.left = Mario.left
            Mario.right = 1
            Ground.right = Mario.right
            Sky.right = Mario.right
            Object.right = Mario.right
            Object2.right = Mario.right
            Object3.right = Mario.right
            Object4.right = Mario.right
            Object5.right = Mario.right
            Goomba.right = Mario.right
            Mario.Wait = 0
        elif event == LEFT_DOWN:
            Mario.velocity -= RUN_SPEED_PPS
            Mario.left = 1
            Ground.left = Mario.left
            Sky.left = Mario.left
            Object.left = Mario.left
            Object2.left = Mario.left
            Object3.left = Mario.left
            Object4.left = Mario.left
            Object5.left = Mario.left
            Goomba.left = Mario.left
            Mario.right = 0
            Ground.right = Mario.right
            Sky.right = Mario.right
            Object.right = Mario.right
            Object2.right = Mario.right
            Object3.right = Mario.right
            Object4.right = Mario.right
            Object5.right = Mario.right
            Goomba.right = Mario.right
            Mario.Wait = 0
        elif event == RIGHT_UP:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Mario.velocity += RUN_SPEED_PPS

    def exit(Mario, event):
        pass

    def do(Mario):
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if Mario.x >= 10 and Mario.x <= 250:
            Mario.x += Mario.velocity * game_framework.frame_time
            Ground.x = Mario.x
            Sky.x = Mario.x
            Object.x = Mario.x
            Object2.x = Mario.x
            Object3.x = Mario.x
            Object4.x = Mario.x
            Object5.x = Mario.x
            Goomba.x = Mario.x

    def draw(Mario):
        if Mario.right == 1:
            if Mario.mode == 0:
                Mario.mario.clip_draw(int(Mario.frame) * 50, 50, 50, 50, Mario.x, Mario.y)
            # else:
            #     walk.clip_+draw(frame * 50, 50, 50, 50, x, y)
        elif Mario.left == 1:
            if Mario.mode == 0:
                Mario.mario.clip_draw((7 - int(Mario.frame)) * 50, 0, 50, 50, Mario.x, Mario.y - 5)
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
    MjumpState: {WAIT: WalkState, RIGHT_DOWN: WalkState,
                 LEFT_DOWN: WalkState, RIGHT_UP: MjumpState,
                 LEFT_UP: MjumpState}
}

class Mario:
    def __init__(self):
        self.Start = 1
        self.mode = 0
        self.i = 0
        self.left = 0
        self.right = 1
        # right, left 변수를 dir로 통일하여 변경할 것
        self.last = 1
        self.x = 0
        self.y = 95
        self.Wait = 0
        self.Jump = 0
        self.jj = 0
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0
        self.velocity = 0
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

    def get_bb(self):
        return self.x - 15, self.y - 20, self.x + 15, self.y + 20

    def stop(self):
        pass

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
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        global x, left, right, Wait, Jump, Attack1, Attack3, keep
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