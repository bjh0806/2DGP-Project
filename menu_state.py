from pico2d import *
import game_framework
import main_state

name = "MenuState"
image = None

def enter():
    global image
    image = load_image('stage_select.png')

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
                game_framework.change_state(main_state)
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.pop_state()

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass