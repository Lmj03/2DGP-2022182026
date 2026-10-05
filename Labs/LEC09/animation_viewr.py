"""Sonic 스프라이트 애니메이션 뷰어."""

from pathlib import Path
from dataclasses import dataclass

from pico2d import (
    SDL_QUIT,
    clear_canvas,
    close_canvas,
    delay,
    get_events,
    load_image,
    open_canvas,
    update_canvas,
)


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SPRITE_PATH = Path(__file__).resolve().with_name("sonic-sprite.png")
SPRITE_WIDTH = 399
SPRITE_HEIGHT = 525
DISPLAY_SCALE = 4
ANIMATION_PAUSE = 1.0
MOVEMENT_START_X = 120
MOVEMENT_END_X = 1080


@dataclass(frozen=True)
class Frame:
    left: int
    top: int
    width: int
    height: int


@dataclass(frozen=True)
class Animation:
    name: str
    frames: tuple[Frame, ...]
    frame_delay: float
    repeat_count: int = 5
    movement_start_x: int | None = None
    movement_end_x: int | None = None


def make_row_frames(top: int, height: int, spans: tuple[tuple[int, int], ...]) -> tuple[Frame, ...]:
    return tuple(
        Frame(left, top, right - left + 1, height)
        for left, right in spans
    )


def source_rectangle(frame: Frame) -> tuple[int, int, int, int]:
    bottom = SPRITE_HEIGHT - frame.top - frame.height
    return frame.left, bottom, frame.width, frame.height


def validate_animations(animations: tuple[Animation, ...]) -> None:
    if not animations:
        raise ValueError("등록된 애니메이션이 없습니다.")

    for animation in animations:
        if not animation.frames:
            raise ValueError(f"프레임이 비어 있는 동작입니다: {animation.name}")
        for frame in animation.frames:
            if frame.width <= 0 or frame.height <= 0:
                raise ValueError(f"프레임 크기가 잘못되었습니다: {animation.name}")
            if frame.left < 0 or frame.top < 0:
                raise ValueError(f"프레임 위치가 잘못되었습니다: {animation.name}")
            if frame.left + frame.width > SPRITE_WIDTH or frame.top + frame.height > SPRITE_HEIGHT:
                raise ValueError(f"프레임이 이미지 영역을 벗어났습니다: {animation.name}")


def draw_frame(sprite_sheet, frame: Frame) -> None:
    left, bottom, width, height = source_rectangle(frame)
    sprite_sheet.clip_draw(
        left,
        bottom,
        width,
        height,
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT // 2,
        width * DISPLAY_SCALE,
        height * DISPLAY_SCALE,
    )


def window_was_closed() -> bool:
    return any(event.type == SDL_QUIT for event in get_events())


def play_animation_once(sprite_sheet, animation: Animation) -> bool:
    for frame in animation.frames:
        if window_was_closed():
            return False
        clear_canvas()
        draw_frame(sprite_sheet, frame)
        update_canvas()
        delay(animation.frame_delay)
    return True


def play_animation(sprite_sheet, animation: Animation) -> bool:
    for _ in range(animation.repeat_count):
        if not play_animation_once(sprite_sheet, animation):
            return False
    delay(ANIMATION_PAUSE)
    return True


def play_all_animations(sprite_sheet) -> None:
    while True:
        for animation in ANIMATIONS:
            if not play_animation(sprite_sheet, animation):
                return


run_animation = Animation(
    "달리기",
    make_row_frames(
        39,
        39,
        ((1, 29), (31, 56), (58, 86), (88, 115), (118, 147), (150, 179), (182, 210), (213, 241), (244, 268), (270, 293), (302, 330)),
    ),
    0.1,
    movement_start_x=MOVEMENT_START_X,
    movement_end_x=MOVEMENT_END_X,
)

action_animation = Animation(
    "동작",
    make_row_frames(
        79,
        39,
        ((8, 33), (37, 63), (65, 95), (97, 133), (135, 166), (170, 201), (206, 231), (238, 261), (263, 292), (295, 330), (334, 365), (370, 398)),
    ),
    0.1,
)

jump_animation = Animation(
    "점프",
    make_row_frames(
        121,
        43,
        ((1, 33), (39, 73), (89, 123), (130, 163), (181, 214), (228, 260)),
    ),
    0.15,
)

spin_animation = Animation(
    "회전",
    make_row_frames(
        167,
        33,
        ((1, 29), (35, 63), (67, 96), (98, 128), (131, 159), (162, 190), (193, 222), (230, 260), (268, 297)),
    ),
    0.1,
)

roll_animation = Animation(
    "구르기",
    make_row_frames(
        206,
        27,
        ((1, 30), (36, 64), (70, 98), (105, 133), (139, 167), (174, 202)),
    ),
    0.1,
    movement_start_x=MOVEMENT_START_X,
    movement_end_x=MOVEMENT_END_X,
)

attack_animation = Animation(
    "공격",
    make_row_frames(
        238,
        36,
        ((1, 29), (36, 65), (74, 104), (111, 141), (149, 178), (186, 216)),
    ),
    0.1,
)

slide_animation = Animation(
    "미끄러지기",
    make_row_frames(
        283,
        35,
        ((1, 29), (36, 65), (72, 110), (123, 161), (172, 210), (218, 255)),
    ),
    0.1,
    movement_start_x=MOVEMENT_START_X,
    movement_end_x=MOVEMENT_END_X,
)

fall_animation = Animation(
    "낙하",
    make_row_frames(
        326,
        45,
        ((1, 24), (31, 59), (65, 84), (90, 114), (119, 143), (149, 168), (184, 223), (232, 270)),
    ),
    0.12,
)

walk_animation = Animation(
    "걷기",
    make_row_frames(
        377,
        40,
        ((1, 27), (31, 61), (64, 94), (99, 131), (136, 167), (176, 208), (217, 249), (254, 286)),
    ),
    0.12,
    movement_start_x=MOVEMENT_START_X,
    movement_end_x=MOVEMENT_END_X,
)

special_animation = Animation(
    "특수 동작",
    make_row_frames(
        426,
        43,
        ((6, 39), (49, 82), (96, 118), (125, 147)),
    ),
    0.15,
)

ANIMATIONS: tuple[Animation, ...] = (run_animation, action_animation, jump_animation, spin_animation, roll_animation, attack_animation, slide_animation, fall_animation, walk_animation, special_animation)


def main():
    open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
    try:
        if not SPRITE_PATH.is_file():
            raise FileNotFoundError(f"스프라이트 이미지를 찾을 수 없습니다: {SPRITE_PATH}")
        sprite_sheet = load_image(str(SPRITE_PATH))
        validate_animations(ANIMATIONS)
        play_all_animations(sprite_sheet)
    finally:
        close_canvas()


if __name__ == "__main__":
    main()