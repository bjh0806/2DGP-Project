from pico2d import *
import game_framework

from sky import Sky
from ground import Ground
from object import Object

name = "MainState"

sky = None
ground = None
object = None

def enter():
    global sky, ground, object
    sky = Sky()
    ground = Ground()
    object = Object()

def exit():
    global sky, ground, object
    del sky
    del ground
    del object

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
    object.update_random_box()
    object.update()
    delay(0.05)
    
def draw():
    clear_canvas()
    sky.draw()
    ground.draw()
    object.draw_random_box()
    object.draw_upground()
    object.draw_upground2()
    object.draw_coin()
    update_canvas()