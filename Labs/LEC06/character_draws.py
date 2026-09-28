# 실습 과제 진행
from pico2d import *
import math
#맨처음 해야할 일은 open_canvas
open_canvas(800, 600)
character = load_image('character.png')

def move_circle():
   for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)

def move_rectangle():
    print('rectangle')
    pass

def move_triangle():
    print('triangle')
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()