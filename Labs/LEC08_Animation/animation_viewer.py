from pico2d import *
# 공격은 9, 구르기는 5, 점프는 7, 걷기는 8, 달리기는 6프레임
# 공격 프레임은 3~6프레임의 크기는 200x200임.
open_canvas()
character = load_image('Project_Spritesheet.png')

def Attack_Ani():
    for frame in range(9):
        clear_canvas()
        character.clip_draw(
            frame * 180, 50, 
            150, 150, 
            350, 300
        )
        update_canvas()
        delay(0.5)

while True:
    Attack_Ani()
    pass