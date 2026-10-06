from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.05
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


def handle_events(running):
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
    return running


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    ground = load_image(str(GROUND_PATH))
    character = load_image(str(CHARACTER_PATH))
    running = True
    x = CANVAS_WIDTH // 2
    y = CANVAS_HEIGHT // 2
    frame = 0
    while running:
        clear_canvas()
        ground.draw_to_fit(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT)
        character.clip_draw(
            frame * FRAME_WIDTH,
            IDLE_RIGHT_ROW,
            FRAME_WIDTH,
            FRAME_HEIGHT,
            x,
            y,
        )
        update_canvas()
        running = handle_events(running)
        frame = (frame + 1) % FRAME_COUNT
        delay(FRAME_DELAY)
    close_canvas()


if __name__ == '__main__':
    main()