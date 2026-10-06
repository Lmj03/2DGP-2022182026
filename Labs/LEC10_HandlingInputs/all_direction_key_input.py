from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
FRAME_DELAY = 0.05
MOVE_SPEED = 8
BOUNDARY_MARGIN = 25
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
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


def load_resources():
    missing_paths = [
        path for path in (GROUND_PATH, CHARACTER_PATH) if not path.exists()
    ]
    if missing_paths:
        missing_files = ', '.join(str(path) for path in missing_paths)
        raise FileNotFoundError(f'이미지 파일을 찾을 수 없습니다: {missing_files}')
    return load_image(str(GROUND_PATH)), load_image(str(CHARACTER_PATH))


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        ground, character = load_resources()
    except FileNotFoundError as error:
        print(error)
        close_canvas()
        return
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
        x = max(BOUNDARY_MARGIN, min(CANVAS_WIDTH - BOUNDARY_MARGIN, x))
        y = max(BOUNDARY_MARGIN, min(CANVAS_HEIGHT - BOUNDARY_MARGIN, y))
        if is_moving:
            animation_row = (
                MOVE_RIGHT_ROW if facing_direction > 0 else MOVE_LEFT_ROW
            )
        else:
            animation_row = (
                IDLE_RIGHT_ROW if facing_direction > 0 else IDLE_LEFT_ROW
            )
        clear_canvas()
        ground.clip_draw(
            (ground.w - CANVAS_WIDTH) // 2,
            (ground.h - CANVAS_HEIGHT) // 2,
            CANVAS_WIDTH,
            CANVAS_HEIGHT,
            CANVAS_WIDTH // 2,
            CANVAS_HEIGHT // 2,
        )
        draw_character(character, x, y, frame, animation_row)
        update_canvas()
        running = handle_events(running, keys)
        frame = (frame + 1) % FRAME_COUNT
        delay(FRAME_DELAY)
    close_canvas()


if __name__ == '__main__':
    main()