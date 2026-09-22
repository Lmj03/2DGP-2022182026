from pico2d import *
import math
open_canvas(800,600)

grass = load_image('grass.png')
character = load_image('character.png')
'''
x = 20
y = 90
state = 'right'
while True:
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,y)

    if state == 'right':
        x += 2
        if x >780:
            state = 'up'
    elif state == 'up':
        y+=2
        if(y>570):
            state = 'left'
    elif state == 'left':
        x-=2
        if(x<20):
            state = 'down'
    elif state == 'down':
        y-=2
        if(y<90):
            state = 'right'

    update_canvas()
    delay(0.01)
'''
x = 400
y = 30
radius = 200
angle = 0
while True:
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    x = 400 + (radius * math.cos(math.radians(angle)))
    y = 300 + (radius * math.sin(math.radians(angle)))
    angle += 2

    update_canvas()
    delay(0.01)