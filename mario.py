from pico2d import *
import random
import game_framework
import start_state

name = "MainState"

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
dir = 0
Wait = 0
Jump = 0
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

class Ground:
    def __init__(self):
        self.ground = load_image('ground.png')

    def draw(self):
        self.ground.draw(groundw, groundh)

class Mario:
    def __init__(self):
        self.Start = 1
        self.mode = 0
        self.i = 0
        self.x, self.y = 0, 95
        self.firstframe = 0
        self.waitframe = 0
        self.frame = 0
        self.jumpframe = 0
        self.start = load_image('start.png')
        self.wait = load_image('wait.png')
        self.mario = load_image('mario.png')
        self.jump = load_image('jump.png')

    def update(self):
        global Wait, skyw, groundw, i, skyh, groundh, upgroundh, upground2h, Jump, x1, x2, x3, y1, y2, y3

        if self.Start == 1:
            self.firstframe = (self.firstframe + 1) % 10
            self.x += 7
            if self.firstframe == 9:
                global Wait
                Wait = 1
                self.Start = 0
                self.firstframe = 0

        elif Wait == 1:
            self.waitframe = (self.waitframe + 1) % 7

        elif Jump == 1:
            if i == 0:
                if right == 1:
                    x1, y1 = self.x, self.y
                    x3, y3 = self.x + 20, self.y
                    x2, y2 = self.x + 10, self.y + 75
                elif left == 1:
                    x1, y1 = self.x, self.y
                    x3, y3 = self.x - 20, self.y
                    x2, y2 = self.x - 10, self.y + 75

            t = i / 100

            self.x = (2 * t ** 2 - 3 * t + 1) * x1 + (-4 * t ** 2 + 4 * t) * x2 + (2 * t ** 2 - t) * x3
            self.y = (2 * t ** 2 - 3 * t + 1) * y1 + (-4 * t ** 2 + 4 * t) * y2 + (2 * t ** 2 - t) * y3

            i += 4

            if right == 1:
                if self.x < x2:
                    skyh -= 2
                    groundh -= 2
                    # firey -= 2
                    for j in range(0, len(random_boxw)):
                        random_boxh[j] -= 2
                    upgroundh -= 2
                    upground2h -= 2
                    for m in range(0, len(coinw)):
                        coinh[m] -= 2
                else:
                    skyh += 2
                    groundh += 2
                    for j in range(0, len(random_boxw)):
                        random_boxh[j] += 2
                    upgroundh += 2
                    upground2h += 2
                    for m in range(0, len(coinw)):
                        coinh[m] += 2
            elif left == 1:
                if self.x < x2:
                    skyh += 2
                    groundh += 2
                    for j in range(0, len(random_boxw)):
                        random_boxh[j] += 2
                    upgroundh += 2
                    upground2h += 2
                    for m in range(0, len(coinw)):
                        coinh[m] += 2
                else:
                    skyh -= 2
                    groundh -= 2
                    for j in range(0, len(random_boxw)):
                        random_boxh[j] -= 2
                    upgroundh -= 2
                    upground2h -= 2
                    for m in range(0, len(coinw)):
                        coinh[m] -= 2

            if i == 104:
                Jump = 0
                Wait = 1
                i = 0

            self.jumpframe = (self.jumpframe + 1) % 14

            if right == 1:
                skyw -= 5 // 2
                groundw -= 7
                for j in range(0, len(random_boxw)):
                    random_boxw[j] -= 7
                for k in range(0, len(upgroundw)):
                    upgroundw[k] -= 7
                for l in range(0, len(upground2w)):
                    upground2w[l] -= 7
                for m in range(0, len(coinw)):
                    coinw[m] -= 7
            elif left == 1:
                skyw += 5 // 2
                groundw += 7
                for j in range(0, len(random_boxw)):
                    random_boxw[j] += 7
                for k in range(0, len(upgroundw)):
                    upgroundw[k] += 7
                for l in range(0, len(upground2w)):
                    upground2w[l] += 7
                for m in range(0, len(coinw)):
                    coinw[m] += 7

        else:
            self.frame = (self.frame + 1) % 8
            if self.x >= 10 and self.x <= 250:
                self.x += dir * 5
            skyw -= dir * 5 // 2
            groundw -= dir * 7

    def draw(self):
        global Wait, Jump, skyh, groundh, upgroundh, upground2h, i

        if self.Start == 1:
            self.start.clip_draw(self.firstframe * 50, 0, 50, 50, self.x, self.y)

        if Wait == 1:
            if right == 1:
                if self.mode == 0:
                    self.wait.clip_draw(self.waitframe * 50, 50, 50, 50, self.x, self.y)
                # else:
                #     modewait.clip_draw(waitframe * 50, 50, 50, 50, x, y)
            elif left == 1:
                if self.mode == 0:
                    self.wait.clip_draw(self.waitframe * 50, 0, 50, 50, self.x, self.y)
                # else:
                #     modewait.clip_draw(waitframe * 50, 0, 50, 50, x, y)

        elif Jump == 1:
            if right == 1:
                if self.mode == 0:
                    self.jump.clip_draw((self.jumpframe + 5) * 50, 50, 50, 50, self.x, self.y)
                # else:
                #     modejump.clip_draw(jumpframe * 50, 50, 50, 50, x, y)
            elif left == 1:
                if self.mode == 0:
                    self.jump.clip_draw((13 - self.jumpframe) * 50, 0, 50, 50, self.x, self.y)
                # else:
                #     modejump.clip_draw((13 - jumpframe) * 50, 0, 50, 50, x, y)

        elif right == 1:
            if self.mode == 0:
                self.mario.clip_draw(self.frame * 50, 50, 50, 50, self.x, self.y)
            # else:
            #     walk.clip_draw(frame * 50, 50, 50, 50, x, y)
        elif left == 1:
            if self.mode == 0:
                self.mario.clip_draw((7 - self.frame) * 50, 0, 50, 50, self.x, self.y - 5)
            # else:
            #     self.walk.clip_draw((7 - self.frame) * 50, 0, 50, 50, self.x, self.y)

class Object:
    upground = None
    upground2 = None

    def __init__(self):
        self.random_box = load_image('random_box.png')
        self.randomframe = random.randint(0, 3)
        if Object.upground == None:
            Object.upground = load_image('upground.png')
        if Object.upground2 == None:
            Object.upground2 = load_image('upground_double.png')
        self.coin = load_image('coin.png')

    def update_random_box(self):
        self.randomframe = (self.randomframe + 1) % 4

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
        if event.type == SDL_QUIT:
            game_framework.quit()
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
                game_framework.change_state(start_state)
            elif event.key == SDLK_SPACE:
                Jump = 1
                Wait = 0
            elif event.key == SDLK_z:
                Attack1 = 1
                Wait = 0
            elif event.key == SDLK_LCTRL:
                if mode == 1:
                    Attack3 = 1
                    keep = 1
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

def update():
    handle_events()
    object.update_random_box()
    mario.update()
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
#     elif right == 1:
#         if mode == 0:
#             mario.clip_draw(frame * 50, 50, 50, 50, x, y)
#         else:
#             walk.clip_draw(frame * 50, 50, 50, 50, x, y)
#     elif left == 1:
#         if mode == 0:
#             mario.clip_draw((7 - frame) * 50, 0, 50, 50, x, y - 5)
#         else:
#             walk.clip_draw((7 - frame) * 50, 0, 50, 50, x, y)
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
#     else:
#         frame = (frame + 1) % 8
#         if x >= 10 and x <= 250:
#             x += dir * 5
#         skyw -= dir * 5 // 2
#         groundw -= dir * 7
#         for j in range(0, len(random_boxw)):
#             random_boxw[j] -= dir * 7
#         for k in range(0, len(upgroundw)):
#             upgroundw[k] -= dir * 7
#         for l in range(0, len(upground2w)):
#             upground2w[l] -= dir * 7
#         for m in range(0, len(coinw)):
#             coinw[m] -= dir * 7
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