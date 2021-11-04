name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('title.png')

def exit():
    global image
    del(image)

def update():
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        game_framework.quit()
    delay(0.01)
    logo_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(800, 600)
    update_canvas()