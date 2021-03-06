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
from turtle import Turtle
from door import Door
from mflower import Mflower
from background import Background
from bowser import Bowser
from ball import Ball
from flower import Flower

name = "MainState"

def enter():
    server.menu_bgm.stop()
    server.object6 = Object6()
    server.mario = Mario()
    server.ball = Ball()
    server.flower = Flower()

    if server.stage == 1 or server.stage == 2 or server.stage == 3 or server.stage == 4:
        server.sky = Sky()
        server.ground = Ground()
        server.door = Door()

    if server.stage == 5:
        server.boss_bgm = load_music('boss_music.mp3')
        server.boss_bgm.set_volume(64)
        server.boss_bgm.repeat_play()

        server.background = Background()
        server.bowser = Bowser()

    if server.stage == 1:
        server.main1_bgm = load_music('main1_music.mp3')
        server.main1_bgm.set_volume(64)
        server.main1_bgm.repeat_play()

        server.objects1 = [Object(i) for i in server.object1w]
        game_world.add_objects(server.objects1, 1)

        server.objects2 = [Object2(i) for i in server.object2w]
        game_world.add_objects(server.objects2, 1)

        server.objects3 = [Object3(i, j) for i, j in server.object3w]
        game_world.add_objects(server.objects3, 1)

        server.objects4 = [Object4(i, j) for i, j in server.object4w]
        game_world.add_objects(server.objects4, 1)

        server.objects5 = [Object5(i, j) for i, j in server.object5w]
        game_world.add_objects(server.objects5, 1)

        server.goombas = [Goomba(i) for i in server.goombaw]
        game_world.add_objects(server.goombas, 1)

    if server.stage == 2:
        server.main2_bgm = load_music('main2_music.mp3')
        server.main2_bgm.set_volume(64)
        server.main2_bgm.repeat_play()

        server.objects1 = [Object(i) for i in server.object1w2]
        game_world.add_objects(server.objects1, 1)

        server.objects2 = [Object2(i) for i in server.object2w2]
        game_world.add_objects(server.objects2, 1)

        server.objects3 = [Object3(i, j) for i, j in server.object3w2]
        game_world.add_objects(server.objects3, 1)

        server.objects4 = [Object4(i, j) for i, j in server.object4w2]
        game_world.add_objects(server.objects4, 1)

        server.objects5 = [Object5(i, j) for i, j in server.object5w2]
        game_world.add_objects(server.objects5, 1)

        server.goombas = [Goomba(i) for i in server.goombaw2]
        game_world.add_objects(server.goombas, 1)

        server.turtles = [Turtle(i, j) for i, j in server.turtlew2]
        game_world.add_objects(server.turtles, 1)

    if server.stage == 3:
        server.main3_bgm = load_music('main3_music.mp3')
        server.main3_bgm.set_volume(64)
        server.main3_bgm.repeat_play()

        server.objects1 = [Object(i) for i in server.object1w3]
        game_world.add_objects(server.objects1, 1)

        server.objects2 = [Object2(i) for i in server.object2w3]
        game_world.add_objects(server.objects2, 1)

        server.objects3 = [Object3(i, j) for i, j in server.object3w3]
        game_world.add_objects(server.objects3, 1)

        server.objects4 = [Object4(i, j) for i, j in server.object4w3]
        game_world.add_objects(server.objects4, 1)

        server.turtles = [Turtle(i, j) for i, j in server.turtlew3]
        game_world.add_objects(server.turtles, 1)

        server.mflowers = [Mflower(i) for i in server.mflowerw3]
        game_world.add_objects(server.mflowers, 1)

    if server.stage == 4:
        server.main4_bgm = load_music('main4_music.mp3')
        server.main4_bgm.set_volume(50)
        server.main4_bgm.repeat_play()

        server.objects1 = [Object(i) for i in server.object1w4]
        game_world.add_objects(server.objects1, 1)

        server.objects2 = [Object2(i) for i in server.object2w4]
        game_world.add_objects(server.objects2, 1)

        server.objects3 = [Object3(i, j) for i, j in server.object3w4]
        game_world.add_objects(server.objects3, 1)

        server.objects4 = [Object4(i, j) for i, j in server.object4w4]
        game_world.add_objects(server.objects4, 1)

        server.objects5 = [Object5(i, j) for i, j in server.object5w4]
        game_world.add_objects(server.objects5, 1)

    if server.stage == 1 or server.stage == 2 or server.stage == 3 or server.stage == 4:
        game_world.add_object(server.sky, 0)
        game_world.add_object(server.ground, 0)
        game_world.add_object(server.door, 0)

    if server.stage == 5:
        game_world.add_object(server.background, 0)
        game_world.add_object(server.bowser, 1)
        game_world.add_object(server.ball, 1)
        game_world.add_object(server.flower, 1)
        server.objects5 = [Object5(i, j) for i, j in server.object5w5]
        game_world.add_objects(server.objects5, 1)

    game_world.add_object(server.object6, 1)
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
            game_framework.change_state(menu_state)
            server.heartcount = 3
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