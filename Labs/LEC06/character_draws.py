# 실습 과제 진행
from pico2d import *
import math
#맨처음 해야할 일은 open_canvas
open_canvas(800, 600)
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)
    
def draw_top():
    for x in range(750, 50, -5):
        draw_character(x, 550)

def draw_left():
    for y in range(550, 50, -5):
        draw_character(50, y)
        
def draw_bottom():
    for x in range(50, 750, 5):
        draw_character(x, 50)

def draw_right():
    for y in range(50, 550, 5):
        draw_character(750, y)

def draw_leftdia():
    for x in range(50, 400, 5):
        y = 50 + (x - 50) * (500 / 350)
        draw_character(x, y)

def draw_bottomline():
    print("bottomline")
    pass

def draw_rightdia():
    for x in range(400, 750, 5):
        y = 500 - (x - 400) * (500 / 350)
        draw_character(x, y)

def move_circle():
   for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_character(x, y)

def move_rectangle():
    draw_top()
    draw_left()
    draw_bottom()
    draw_right()
    pass

def move_triangle():
    draw_leftdia()
    draw_rightdia()
    draw_bottomline()
    pass

while True:
    # move_circle()
    # move_rectangle()
    move_triangle()
    pass

close_canvas()