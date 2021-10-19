from pico2d import *

Back_WIDTH, Back_HEIGHT = 1600, 900

open_canvas(Back_WIDTH, Back_HEIGHT)

background = load_image('background.png')

background.draw(Back_WIDTH // 2, Back_HEIGHT // 2)

delay(5)

close_canvas()