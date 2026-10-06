from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.05
MOVE_SPEED = 4
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
FRAME_COUNT = 8
IDLE_RIGHT_ROW = 300
IDLE_LEFT_ROW = 200
MOVE_RIGHT_ROW = 100
MOVE_LEFT_ROW = 0


RESOURCE_DIR = Path(__file__).resolve().parent
GROUND_PATH = RESOURCE_DIR / 'TUK_GROUND.png'
CHARACTER_PATH = RESOURCE_DIR / 'animation_sheet.png'


def handle_events(running, keys):
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key in keys:
            keys[event.key] = True
        elif event.type == SDL_KEYUP and event.key in keys:
            keys[event.key] = False
    return running


def get_movement(keys):
    horizontal = int(keys[SDLK_RIGHT]) - int(keys[SDLK_LEFT])
    vertical = int(keys[SDLK_UP]) - int(keys[SDLK_DOWN])
    return horizontal, vertical


def draw_character(character, x, y, frame, animation_row):
    character.clip_draw(
        frame * FRAME_WIDTH,
        animation_row,
        FRAME_WIDTH,
        FRAME_HEIGHT,
        x,
        y,
    )


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    ground = load_image(str(GROUND_PATH))
    character = load_image(str(CHARACTER_PATH))
    running = True
    x = CANVAS_WIDTH // 2
    y = CANVAS_HEIGHT // 2
    frame = 0
    facing_direction = 1
    keys = {
        SDLK_UP: False,
        SDLK_DOWN: False,
        SDLK_LEFT: False,
        SDLK_RIGHT: False,
    }
    while running:
        horizontal, vertical = get_movement(keys)
        if horizontal > 0:
            facing_direction = 1
        elif horizontal < 0:
            facing_direction = -1
        x += horizontal * MOVE_SPEED
        y += vertical * MOVE_SPEED
        is_moving = horizontal != 0 or vertical != 0
        half_width = FRAME_WIDTH // 2
        half_height = FRAME_HEIGHT // 2
        x = max(half_width, min(CANVAS_WIDTH - half_width, x))
        y = max(half_height, min(CANVAS_HEIGHT - half_height, y))
        idle_row = IDLE_RIGHT_ROW if facing_direction > 0 else IDLE_LEFT_ROW
        animation_row = idle_row
        clear_canvas()
        ground.draw_to_fit(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
        draw_character(character, x, y, frame, animation_row)
        update_canvas()
        running = handle_events(running, keys)
        frame = (frame + 1) % FRAME_COUNT
        delay(FRAME_DELAY)
    close_canvas()


if __name__ == '__main__':
    main()