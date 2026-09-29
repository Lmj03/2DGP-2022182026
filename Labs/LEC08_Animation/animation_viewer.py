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
    (1700, 48, 88, 118)
]

Roll_Sprites_cordinate = [
    (47, 278, 104, 81),
    (218, 278, 114, 75),
    (395, 278, 89, 100),
    (548, 278, 94, 84),
    (710, 278, 100, 78)
]

Jump_Sprites_cordinate = [
    (52, 447, 96, 98),
    (227, 448, 87, 134),
    (389, 466, 82, 154),
    (542, 484, 84, 106),
    (702, 467, 106, 125),
    (884, 448, 102, 87),
    (1068, 448, 74, 139)
]

Run_Sprites_cordinate = [
    (59,   698, 95,  126),
    (224,  711, 132, 115),
    (418,  698, 96,  125),
    (600,  698, 89,  122),
    (779,  699, 97,  123),
    (939,  709, 141, 117),
    (1139, 700, 97,  123),
    (1320, 697, 88,  123)
]

Walk_Sprites_cordinate = [
    (64, 878, 80, 126),
    (243, 878, 82, 127),
    (425, 878, 79, 127),
    (603, 878, 82, 127),
    (784, 878, 82, 128),
    (964, 878, 82, 127)
]

def Playing_Ani(frame, Sprites_cordinate, delay_time):
    for i in range(frame):
        clear_canvas()
        character.clip_draw(
            Sprites_cordinate[i][0], Sprites_cordinate[i][1], 
            Sprites_cordinate[i][2], Sprites_cordinate[i][3], 
            400, 300
        )
        update_canvas()
        delay(delay_time)
    

def Attack_Ani():
    Playing_Ani(9, Attack_Sprites_cordinate, 0.1)

def Roll_Ani():
    Playing_Ani(5, Roll_Sprites_cordinate, 0.1)

def Jump_Ani():
    Playing_Ani(7, Jump_Sprites_cordinate, 0.2)

def Run_Ani():
    Playing_Ani(8, Run_Sprites_cordinate, 0.1)
    
def walk_Ani():
    Playing_Ani(6, Walk_Sprites_cordinate, 0.1)
    
while True:
    # Attack_Ani()
    # Roll_Ani()
    # Jump_Ani()
    # Run_Ani()
    walk_Ani()
    pass