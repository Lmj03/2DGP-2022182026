from math import pi

from pico2d import load_image, get_time, SDL_KEYDOWN, SDLK_SPACE
from transitions import Machine


class Boy:
    IDLE_TIMEOUT = 5.0

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.face_dir = 1
        self.image = load_image('animation_sheet.png')
        self.state_machine = Machine(
            model=self,
            states=[
                {'name': 'IDLE', 'on_enter': 'enter_idle'},
                {'name': 'SLEEP', 'on_enter': 'enter_sleep'},
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
            ],
        )
        # Machine does not call on_enter when assigning the initial state.
        self.enter_idle()

    def enter_idle(self):
        self.frame = 0
        self.idle_start_time = get_time()

    def enter_sleep(self):
        self.frame = 0

    def idle_time_elapsed(self):
        return get_time() - self.idle_start_time >= self.IDLE_TIMEOUT

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and self.is_SLEEP():
            self.wake_up()

    def update(self):
        self.tick()

    def animate_idle(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        row = 300 if self.face_dir == 1 else 200
        if self.is_IDLE():
            self.image.clip_draw(self.frame * 100, row, 100, 100, self.x, self.y)
        elif self.is_SLEEP():
            # Rotate the first IDLE frame 90 degrees and lower it to the ground.
            self.image.clip_composite_draw(
                0, row, 100, 100, pi / 2, '', self.x, self.y - 15, 100, 100
            )
