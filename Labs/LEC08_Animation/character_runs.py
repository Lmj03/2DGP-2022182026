from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

# fill here
frame = 0
def animation_draw(x, sheet_col):
    global frame
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, sheet_col, 100, 100, x, 90)
    update_canvas()
        
    frame = (frame + 1) % 8
    delay(0.05)

def right_run():
    for x in range(50, 750, 10):
        animation_draw(x, 100)

def right_idle():
    for x in range(0, 400, 10):
        animation_draw(750, 300)

def left_idle():
    for x in range(0, 400, 10):
        animation_draw(750, 200)

def left_run():
    for x in range(750, 50, -10):
        animation_draw(x, 0)

right_run()
right_idle()
left_idle()
left_run()


close_canvas()

