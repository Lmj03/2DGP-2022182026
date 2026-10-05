"""Sonic 스프라이트 애니메이션 뷰어."""

from pico2d import close_canvas, open_canvas


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


def main():
    open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
    close_canvas()


if __name__ == "__main__":
    main()