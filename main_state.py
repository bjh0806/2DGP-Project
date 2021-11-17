from pico2d import *
import game_framework
import menu_state
import game_world

from sky import Sky
from ground import Ground
from object import Object
from mario import Mario
from object2 import Object2

name = "MainState"

sky = None
ground = None
object = None
mario = None
object2 = None

def enter():
    global sky, ground, object, mario, object2
    sky = Sky()
    ground = Ground()
    object = Object()
    mario = Mario()
    object2 = Object2()
    game_world.add_object(sky, 0)
    game_world.add_object(ground, 0)
    game_world.add_object(object, 1)
    game_world.add_object(object2, 1)
    game_world.add_object(mario, 1)

def exit():
    game_world.clear()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

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