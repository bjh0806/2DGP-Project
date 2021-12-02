from pico2d import *
import game_framework
import menu_state
import game_world
import server

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

object2w = [850, 2500]
object3w = [(300, 200), (400, 200), (425, 200), (855, 300), (1100, 200), (1600, 200), (1825, 200), (2000, 200), (2025, 200)]
object4w = [(580, 130), (610, 160), (640, 180), (740, 180), (770, 210), (800, 230), (1300, 160), (1330, 190), (1360, 190),
            (1390, 160), (2175, 160), (2205, 190), (2235, 190), (2265, 160)]
object5w = [(1075, 200), (1124, 200), (1800, 200), (1849, 200)]

def enter():
    server.sky = Sky()
    server.ground = Ground()
    server.object6 = Object6()
    server.goomba = Goomba()
    server.mario = Mario()
    
    server.objects1 = [Object(i, 50) for i in object1w]
    game_world.add_objects(server.objects1, 1)

    server.objects2 = [Object2(i, 70) for i in object2w]
    game_world.add_objects(server.objects2, 1)

    server.objects3 = [Object3(i, j) for i, j in object3w]
    game_world.add_objects(server.objects3, 1)

    server.objects4 = [Object4(i, j) for i, j in object4w]
    game_world.add_objects(server.objects4, 1)

    server.objects5 = [Object5(i, j) for i, j in object5w]
    game_world.add_objects(server.objects5, 1)

    game_world.add_object(server.sky, 0)
    game_world.add_object(server.ground, 0)
    game_world.add_object(server.object6, 1)
    game_world.add_object(server.goomba, 1)
    game_world.add_object(server.mario, 1)

def exit():
    game_world.clear()

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
            server.mario.handle_event(event)
            
def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # if collide(mario, goomba):
    #     game_world.remove_object(goomba)
    # for object in objects1.copy():
    #     if collide(mario, object):
    #         mario.stop1()
    # for object2 in objects2.copy():
    #     if collide(mario, object2):
    #         mario.stop1()
    # for object3 in objects3.copy():
    #     if collide(mario, object3):
    #         mario.stop2()
    # for object4 in objects4.copy():
    #     if collide(mario, object4):
    #         game_world.remove_object(object4)
    # for object5 in objects5.copy():
    #     if collide(mario, object5):
    #         mario.stop2()
    delay(0.05)
    
def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()