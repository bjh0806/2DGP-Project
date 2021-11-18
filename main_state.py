from pico2d import *
import game_framework
import menu_state
import game_world

from sky import Sky
from ground import Ground
from object import Object
from mario import Mario
from object2 import Object2
from object3 import Object3
from object4 import Object4
from object5 import Object5
from object6 import Object6
from goomba import Goomba

name = "MainState"

sky = None
ground = None
object = None
mario = None
object2 = None
object3 = None
object4 = None
object5 = None
object6 = None
goomba = None

def enter():
    global sky, ground, object, mario, object2, object3, object4, object5, object6, goomba
    sky = Sky()
    ground = Ground()
    object = Object()
    object2 = Object2()
    object3 = Object3()
    object4 = Object4()
    object5 = Object5()
    object6 = Object6()
    goomba = Goomba()
    mario = Mario()
    game_world.add_object(sky, 0)
    game_world.add_object(ground, 0)
    game_world.add_object(object, 1)
    game_world.add_object(object2, 1)
    game_world.add_object(object3, 1)
    game_world.add_object(object4, 1)
    game_world.add_object(object5, 1)
    game_world.add_object(object6, 1)
    game_world.add_object(goomba, 1)
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

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.push_state(menu_state)
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