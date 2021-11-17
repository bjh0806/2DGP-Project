from pico2d import *
import game_framework
import menu_state
import game_world

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
    game_world.add_object(sky, 0)
    game_world.add_object(ground, 0)
    game_world.add_object(object, 1)
    game_world.add_object(mario, 1)

def exit():
    game_world.clear()

def pause():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(menu_state)
        else:
            mario.handle_event(event)
            
def update():
    for game_object in game_world.all_objects():
        game_object.update()
    delay(0.05)
    
def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()