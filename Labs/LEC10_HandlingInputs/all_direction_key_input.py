from pico2d import *


def handle_events(running):
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
    return running


def main():
    open_canvas()
    running = True
    while running:
        running = handle_events(running)
        delay(0.05)
    close_canvas()


if __name__ == '__main__':
    main()