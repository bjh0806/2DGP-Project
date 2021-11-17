from pico2d import *
import game_framework

from sky import Sky

name = "MainState"

sky = None

def enter():
    global sky
    sky = Sky()

def exit():
    global sky
    del sky

def pause():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(menu_state)
            
def update():
    sky.update()
    
def draw():
    clear_canvas()
    sky.draw()
    update_canvas()