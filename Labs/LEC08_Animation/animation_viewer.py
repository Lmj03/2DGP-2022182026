from pico2d import *
# 공격은 9, 구르기는 5, 점프는 7, 걷기는 8, 달리기는 6프레임
# 공격 프레임은 3~6프레임의 크기는 200x200임.
open_canvas()
character = load_image('Project_Spritesheet.png')

Attack_Sprites_cordinate = [
    (60, 48, 89, 118),
    (234, 48, 103, 115),
    (415, 48, 98, 118),
    (615, 48, 108, 115),
    (840, 48, 120, 116),
    (1052, 48, 158, 116),
    (1295, 48, 130, 114),
    (1512, 47, 104, 118),
    (1700, 48, 88, 118),
]

Roll_Sprites_cordinate = [
    (47, 278, 104, 81),
    (218, 278, 114, 75),
    (395, 278, 89, 100),
    (548, 278, 94, 84),
    (710, 278, 100, 78),
]

def Attack_Ani():
    for frame in range(9):
        clear_canvas()
        character.clip_draw(
            Attack_Sprites_cordinate[frame][0], Attack_Sprites_cordinate[frame][1], 
            Attack_Sprites_cordinate[frame][2], Attack_Sprites_cordinate[frame][3], 
            400, 300
        )
        update_canvas()
        delay(0.1)


def Roll_Ani():
    for frame in range(5):
        clear_canvas()
        character.clip_draw(
            Roll_Sprites_cordinate[frame][0], Roll_Sprites_cordinate[frame][1], 
            Roll_Sprites_cordinate[frame][2], Roll_Sprites_cordinate[frame][3], 
            400, 300
        )
        update_canvas()
        delay(0.1)

while True:
    # Attack_Ani()
    Roll_Ani()
    pass