from . import clock as clock
import threading, time
import Adafruit_PCA9685
from . import settings

REV='REV2.3'

## create a servo control with no threading
class ServoNT():

    def __init__(self, channel=1, freq=92.7, duty = 0):
        self.pwm = Adafruit_PCA9685.PCA9685(0x40)
        self.pwm.set_pwm_freq(freq)
        self.channel = settings.PINS[REV]['servo{}'.format(channel-1)]
        print(self.channel)
        self.duty = duty

    def set(self, duty):
        self.duty = duty

    def pulse(self, duty):
        self.duty = duty
        pos = int(self.duty*4096)
        print(pos)
        self.pwm.set_pwm(self.channel, 0, pos)

