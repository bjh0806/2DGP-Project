from pico2d import *
import game_framework
import start_state

from sky import Sky
from ground import Ground
from object import Object
from mario import Mario

name = "MainState"

sky = None
ground = None
object = None
mario = None

def enter():
    global sky, ground, object, mario
    sky = Sky()
    ground = Ground()
    object = Object()
    mario = Mario()

def exit():
    global sky, ground, object, mario
    del sky
    del ground
    del object
    del mario

def pause():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            mario.handle_event(event)
            
def update():
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