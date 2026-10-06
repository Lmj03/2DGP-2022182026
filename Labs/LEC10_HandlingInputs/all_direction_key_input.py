from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.05


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
    running = True
    while running:
        running = handle_events(running)
        delay(FRAME_DELAY)
    close_canvas()


if __name__ == '__main__':
    main()