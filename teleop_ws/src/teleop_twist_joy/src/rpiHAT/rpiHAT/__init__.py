from rpiHAT.lsm6ds33  import LSM6DS33
from rpiHAT.clock  import Clock
from rpiHAT.servo     import *
from rpiHAT.servont import *
from rpiHAT.RotaryEncoder  import RotaryEncoder
from rpiHAT.settings  import *
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
