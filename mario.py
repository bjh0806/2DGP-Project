from pico2d import *
import game_framework
from ground import Ground
import server
from fire import Fire
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, WAIT, ATTACK1, ATTACK2 = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_a): LEFT_DOWN,
    (SDL_KEYUP, SDLK_d): RIGHT_UP,
    (SDL_KEYUP, SDLK_a): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_z): ATTACK1,
    (SDL_KEYDOWN, SDLK_x): ATTACK2
}

class StartState:
    def enter(Mario, event):
        Mario.Start = 1

    def exit(Mario, event):
        Mario.Start = 0
        Mario.dir = 1

    def do(Mario):
        Mario.firstframe = (Mario.firstframe + 1) % 10
        Mario.x += 7
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
        Mario.ldir = Mario.dir
        Mario.dir = 0
        Mario.velocity = 0

    def exit(Mario, event):
        pass

    def do(Mario):
        if Mario.Wait == 1:
            Mario.waitframe = (Mario.waitframe + 7 * ACTION_PER_TIME * game_framework.frame_time) % 7

    def draw(Mario):
        if Mario.Wait == 1:
            if Mario.ldir == 1:
                if server.mode == 0:
                    Mario.wait.clip_draw(int(Mario.waitframe) * 50, 50, 50, 50, Mario.x, Mario.y)
                else:
                    Mario.modewait.clip_draw(int(Mario.waitframe) * 50, 50, 50, 50, Mario.x, Mario.y)
            elif Mario.ldir == -1:
                if server.mode == 0:
                    Mario.wait.clip_draw(int(Mario.waitframe) * 50, 0, 50, 50, Mario.x, Mario.y)
                else:
                    Mario.modewait.clip_draw(int(Mario.waitframe) * 50, 0, 50, 50, Mario.x, Mario.y)

class AttackState:
    def enter(Mario, event):
        Mario.attack = 1
        Mario.ldir = Mario.dir

    def exit(Mario, event):
        pass

    def do(Mario):
        if Mario.attack == 1:
            Mario.attackframe1 = (Mario.attackframe1 + 1) % 11
            if Mario.attackframe1 == 10:
                Mario.attack = 0
                Mario.attackframe1 = 0
                Mario.add_event(WAIT)

    def draw(Mario):
        if Mario.attack == 1:
            if Mario.ldir == 1:
                Mario.attack1.clip_draw(int(Mario.attackframe1) * 50, 50, 50, 50, Mario.x, Mario.y)
            elif Mario.ldir == -1:
                Mario.attack1.clip_draw((10 - int(Mario.attackframe1)) * 50, 0, 50, 50, Mario.x, Mario.y)

class Attack2State:
    def enter(Mario, event):
        Mario.attack = 1
        Mario.ldir = Mario.dir
        Mario.fire()

    def exit(Mario, event):
        pass

    def do(Mario):
        if Mario.attack == 1:
            Mario.attackframe2 = (Mario.attackframe2 + 1) % 8
            if Mario.attackframe2 == 7:
                Mario.attack = 0
                Mario.attackframe2 = 0
                Mario.add_event(WAIT)

    def draw(Mario):
        if Mario.attack == 1:
            if Mario.ldir == 1:
                Mario.attack2.clip_draw(int(Mario.attackframe2) * 50, 50, 50, 50, Mario.x, Mario.y)
            elif Mario.ldir == -1:
                Mario.attack2.clip_draw((7 - int(Mario.attackframe2)) * 50, 0, 50, 50, Mario.x, Mario.y)

class JumpState:
    def enter(Mario, event):
        if Mario.jj == 0:
            server.jump_sound.play()
        Mario.jj = 1

    def exit(Mario, event):
        pass

    def do(Mario):
        if Mario.jj == 1:
            if Mario.jjcount < 10:
                Mario.y += 7
                Mario.jjcount += 1

            else:
                if Mario.jjcount < 20:
                    Mario.y -= 7
                    Mario.jjcount += 1
                    if Mario.jjcount == 20:
                        Mario.jjcount = 0
                        Mario.dir = Mario.ldir
                        server.ground_sound.play()
                        Mario.add_event(WAIT)

            Mario.jumpframe = (Mario.jumpframe + 14 * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(Mario):
        if Mario.jj == 1:
            if Mario.ldir == 1:
                if server.mode == 0:
                    Mario.jump.clip_draw((int(Mario.jumpframe) + 5) * 50, 50, 50, 50, Mario.x, Mario.y)
                else:
                    Mario.modejump.clip_draw(int(Mario.jumpframe) * 50, 50, 50, 50, Mario.x, Mario.y)
            elif Mario.ldir == -1:
                if server.mode == 0:
                    Mario.jump.clip_draw((13 - int(Mario.jumpframe)) * 50, 0, 50, 50, Mario.x, Mario.y)
                else:
                    Mario.modejump.clip_draw((13 - int(Mario.jumpframe)) * 50, 0, 50, 50, Mario.x, Mario.y)

class MjumpState:
    def enter(Mario, event):
        if Mario.Jump == 0:
            server.jump_sound.play()
        Mario.Jump = 1

    def exit(Mario, event):
        pass

    def do(Mario):
        if Mario.Jump == 1:
            if Mario.dir == 1:
                if Mario.Jcount < 10:
                    Mario.x += 3
                    Mario.y += 7
                    Mario.Jcount += 1

                else:
                    Mario.x += 3
                    Mario.y -= 7

            elif Mario.dir == -1:
                if Mario.Jcount < 10:
                    Mario.x -= 3
                    Mario.y += 7
                    Mario.Jcount += 1

                else:
                    Mario.x -= 3
                    Mario.y -= 7

            Mario.jumpframe = (Mario.jumpframe + 14 * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(Mario):
        if Mario.Jump == 1:
            if Mario.dir == 1:
                if server.mode == 0:
                    Mario.jump.clip_draw((int(Mario.jumpframe) + 5) * 50, 50, 50, 50, Mario.x, Mario.y)
                else:
                    Mario.modejump.clip_draw(int(Mario.jumpframe) * 50, 50, 50, 50, Mario.x, Mario.y)
            elif Mario.dir == -1:
                if server.mode == 0:
                    Mario.jump.clip_draw((13 - int(Mario.jumpframe)) * 50, 0, 50, 50, Mario.x, Mario.y)
                else:
                    Mario.modejump.clip_draw((13 - int(Mario.jumpframe)) * 50, 0, 50, 50, Mario.x, Mario.y)

class WalkState:
    def enter(Mario, event):
        Mario.Wait = 0
        if event == RIGHT_DOWN:
            Mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            Mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            Mario.velocity += RUN_SPEED_PPS

    def exit(Mario, event):
        pass

    def do(Mario):
        Mario.frame = (Mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        Mario.x += Mario.velocity * game_framework.frame_time

    def draw(Mario):
        if Mario.velocity > 0:
            Mario.dir = 1
            if server.mode == 0:
                Mario.mario.clip_draw(int(Mario.frame) * 50, 50, 50, 50, Mario.x, Mario.y)
            else:
                Mario.walk.clip_draw(int(Mario.frame) * 50, 50, 50, 50, Mario.x, Mario.y)
        elif Mario.velocity < 0:
            Mario.dir = -1
            if server.mode == 0:
                Mario.mario.clip_draw((7 - int(Mario.frame)) * 50, 0, 50, 50, Mario.x, Mario.y - 5)
            else:
                Mario.walk.clip_draw((7 - int(Mario.frame)) * 50, 0, 50, 50, Mario.x, Mario.y - 5)

next_state_table = {
    StartState: {WAIT: WaitState, RIGHT_DOWN: StartState,
                 LEFT_DOWN: StartState, RIGHT_UP: StartState,
                 LEFT_UP: StartState},
    WaitState: {SPACE: JumpState, RIGHT_DOWN: WalkState,
                LEFT_DOWN: WalkState, RIGHT_UP: WaitState,
                LEFT_UP: WaitState, ATTACK1: AttackState,
                ATTACK2: Attack2State},
    JumpState: {WAIT: WaitState},
    WalkState: {RIGHT_DOWN: WalkState, LEFT_DOWN: WalkState,
                RIGHT_UP: WaitState, LEFT_UP: WaitState,
                SPACE: MjumpState, ATTACK1: AttackState,
                ATTACK2: Attack2State},
    MjumpState: {WAIT: WaitState, RIGHT_DOWN: MjumpState,
                 LEFT_DOWN: MjumpState, RIGHT_UP: MjumpState,
                 LEFT_UP: MjumpState},
    AttackState: {RIGHT_DOWN: WalkState, LEFT_DOWN: WalkState,
                  WAIT: WaitState, RIGHT_UP: AttackState,
                  LEFT_UP: AttackState},
    Attack2State: {RIGHT_DOWN: WalkState, LEFT_DOWN: WalkState,
                   WAIT: WaitState, RIGHT_UP: Attack2State,
                   LEFT_UP: Attack2State}
}

class Mario:
    def __init__(self):
        self.Start = 1
        self.mode = 0
        self.i = 0
        self.dir = 0
        self.ldir = 0
        self.x = 0
        self.y = 95
        self.Wait = 0
        self.Jump = 0
        self.Jcount = 0
        self.jj = 0
        self.jjcount = 0
        self.x1 = 0
        self.x2 = 0
        self.x3 = 0
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0
        self.timer = 17
        self.attack = 0
        self.velocity = 0
        self.firstframe = 0
        self.waitframe = 0
        self.frame = 0
        self.jumpframe = 0
        self.attackframe1 = 0
        self.fireframe = 0
        self.attackframe2 = 0
        self.start = load_image('start.png')
        self.wait = load_image('wait.png')
        self.mario = load_image('mario.png')
        self.jump = load_image('jump.png')
        self.strong = load_image('strong.png')
        self.attack1 = load_image('attack1.png')
        self.modewait = load_image('modewait.png')
        self.modejump = load_image('modejump.png')
        self.walk = load_image('walk.png')
        self.attack2 = load_image('attack3.png')
        server.ground_sound = load_wav('ground_sound.wav')
        server.ground_sound.set_volume(64)
        server.jump_sound = load_wav('jump_sound.wav')
        server.jump_sound.set_volume(64)
        server.fire_sound = load_wav('fire_sound.wav')
        server.fire_sound.set_volume(64)
        self.event_que = []
        if self.Start == 1:
            self.cur_state = StartState
        else:
            self.cur_state = WaitState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 15, self.y - 20, self.x + 13, self.y + 20

    def fire(self):
        fire = Fire(self.x - 12.5, self.y, self.dir * 7)
        game_world.add_object(fire, 1)
        server.fire_sound.play()
    
    def JumpStop(self):
        self.y += 10
        self.Jump = 0
        self.Jcount = 0
        server.ground_sound.play()
        self.add_event(WAIT)

    def change_state(self, state):
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        if server.mode == 1 and server.do == 0:
            self.timer -= 1
            self.fireframe = (self.fireframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 17
        else:
            self.cur_state.do(self)
            if len(self.event_que) > 0:
                event = self.event_que.pop()
                self.cur_state.exit(self, event)
                self.cur_state = next_state_table[self.cur_state][event]
                self.cur_state.enter(self, event)
            self.x = clamp(50, self.x, 550)

    def draw(self):
        if server.mode == 1 and server.do == 0:
            if self.dir == 1:
                self.strong.clip_draw(int(self.fireframe) * 50, 100, 50, 100, self.x, self.y + 27)
            elif self.dir == -1:
                self.strong.clip_draw((16 - int(self.fireframe)) * 50, 0, 50, 100, self.x, self.y + 27)
            if self.timer < 0:
                server.do = 1
        else:
            self.cur_state.draw(self)

    def handle_event(self, event):
        global x, Wait, Jump, Attack1, Attack3, keep
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

 # elif event.key == SDLK_z:
        #         Attack1 = 1
        #         Wait = 0
        #     elif event.key == SDLK_LCTRL:
        #         if mode == 1:
        #             Attack3 = 1
        #             keep = 1
        #             Wait = 0

# strong = load_image('strong.png')
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