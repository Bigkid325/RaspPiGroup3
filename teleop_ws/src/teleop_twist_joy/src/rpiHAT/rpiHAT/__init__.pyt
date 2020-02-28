from .altimu import *
from .servo import *
from .clock import *

# constants
IDLE = 0
RUNNING = 1
PAUSED = 2
EXITING = 3

# idle function
def idle():
    set_state(IDLE)

# run function
def run():
    set_state(RUNNING)

# pause function
def pause():
    set_state(PAUSED)

# exit function
def exit():
    set_state(EXITING)
