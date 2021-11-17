from pico2d import *
import game_framework

from sky import Sky
from ground import Ground

name = "MainState"

sky = None
ground = None

def enter():
    global sky, ground
    sky = Sky()
    ground = Ground()

def exit():
    global sky, ground
    del sky
    del ground

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
    ground.update()
    
def draw():
    clear_canvas()
    sky.draw()
    ground.draw()
    update_canvas()