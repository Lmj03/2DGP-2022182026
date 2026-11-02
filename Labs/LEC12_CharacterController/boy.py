from math import pi

from pico2d import (
    load_image, get_time, get_canvas_width,
    SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT,
)
from transitions import Machine


class Boy:
    IDLE_TIMEOUT = 5.0
    RUN_SPEED = 200.0  # Pixels per second.
    HALF_WIDTH = 35  # Visible running pixels fit within 34 pixels of the center.
    SLEEP_HALF_WIDTH = 42  # The rotated first IDLE frame is wider.

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.run_dir = 0
        self.held_directions = []
        self.last_update_time = get_time()
        self.frame_time = 0.0
        self.image = load_image('animation_sheet.png')
        self.state_machine = Machine(
            model=self,
            states=[
                {'name': 'IDLE', 'on_enter': 'enter_idle'},
                {'name': 'SLEEP', 'on_enter': 'enter_sleep'},
                {'name': 'RUN', 'on_enter': 'enter_run'},
            ],
            initial='IDLE',
            auto_transitions=False,
            transitions=[
                # Check the timeout before advancing the IDLE animation.
                {'trigger': 'tick', 'source': 'IDLE', 'dest': 'SLEEP',
                 'conditions': 'idle_time_elapsed'},
                {'trigger': 'tick', 'source': 'IDLE', 'dest': None,
                 'after': 'animate_idle'},
                {'trigger': 'tick', 'source': 'SLEEP', 'dest': None},
                {'trigger': 'wake_up', 'source': 'SLEEP', 'dest': 'IDLE'},
                {'trigger': 'start_running', 'source': 'IDLE', 'dest': 'RUN'},
                {'trigger': 'stop_running', 'source': 'RUN', 'dest': 'IDLE'},
                {'trigger': 'tick', 'source': 'RUN', 'dest': None,
                 'after': 'update_run'},
            ],
        )
        # Machine does not call on_enter when assigning the initial state.
        self.enter_idle()

    def enter_idle(self):
        self.frame = 0
        self.idle_start_time = get_time()

    def enter_sleep(self):
        self.frame = 0
        self.run_dir = 0
        self.held_directions.clear()
        self.clamp_x(self.SLEEP_HALF_WIDTH)

    def enter_run(self):
        self.frame = 0

    def idle_time_elapsed(self):
        return get_time() - self.idle_start_time >= self.IDLE_TIMEOUT

    def handle_event(self, event):
        if self.is_SLEEP():
            if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                self.wake_up()
            return

        if event.type not in (SDL_KEYDOWN, SDL_KEYUP):
            return
        if event.key not in (SDLK_LEFT, SDLK_RIGHT):
            return

        if event.type == SDL_KEYDOWN:
            # Keep press order; repeated KEYDOWN must not change priority.
            if event.key not in self.held_directions:
                self.held_directions.append(event.key)
                self.face_dir = 1 if event.key == SDLK_RIGHT else -1
        elif event.key in self.held_directions:
            self.held_directions.remove(event.key)

        # Opposite directions cancel movement, while facing keeps the last press.
        self.run_dir = (int(SDLK_RIGHT in self.held_directions)
                        - int(SDLK_LEFT in self.held_directions))
        if self.run_dir:
            self.face_dir = self.run_dir
            if self.is_IDLE():
                self.start_running()
        elif self.is_RUN():
            self.stop_running()

    def update(self):
        now = get_time()
        self.frame_time = now - self.last_update_time
        self.last_update_time = now
        self.tick()

    def animate_idle(self):
        self.frame = (self.frame + 1) % 8

    def update_run(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.run_dir * self.RUN_SPEED * self.frame_time
        self.clamp_x(self.HALF_WIDTH)

    def clamp_x(self, half_width):
        # Bound the visible character instead of the transparent sprite padding.
        self.x = max(half_width, min(self.x, get_canvas_width() - half_width))

    def draw(self):
        row = 300 if self.face_dir == 1 else 200
        if self.is_IDLE():
            self.image.clip_draw(self.frame * 100, row, 100, 100, self.x, self.y)
        elif self.is_RUN():
            row = 100 if self.face_dir == 1 else 0
            self.image.clip_draw(self.frame * 100, row, 100, 100, self.x, self.y)
        elif self.is_SLEEP():
            # Rotate the first IDLE frame 90 degrees and lower it to the ground.
            self.image.clip_composite_draw(
                0, row, 100, 100, pi / 2, '', self.x, self.y - 30, 100, 100
            )
