from pico2d import *
import game_framework
import server

name = "EndState"
image = None

def enter():
    global image
    image = load_image('win.png')
    server.win_bgm = load_music('win_music.mp3')
    server.win_bgm.set_volume(64)
    server.win_bgm.play()

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass