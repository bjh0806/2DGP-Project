from pico2d import *
import game_framework
import main_state
import server

name = "MenuState"
image = None

def enter():
    global image
    image = load_image('stage_select.png')
    server.open_bgm.stop()
    server.menu_bgm = load_music('select_music.mp3')
    server.menu_bgm.set_volume(64)
    server.menu_bgm.repeat_play()

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.x >= 470 and event.y <= 200 and event.y >= 100:
                server.stage = 1
                game_framework.change_state(main_state)
            if event.x >= 470 and event.y <= 300 and event.y >= 200:
                server.stage = 2
                game_framework.change_state(main_state)
            if event.x >= 470 and event.y <= 400 and event.y >= 300:
                server.stage = 3
                game_framework.change_state(main_state)
            if event.x >= 470 and event.y <= 500 and event.y >= 400:
                server.stage = 4
                game_framework.change_state(main_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_5):
                server.stage = 5
                game_framework.change_state(main_state)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass