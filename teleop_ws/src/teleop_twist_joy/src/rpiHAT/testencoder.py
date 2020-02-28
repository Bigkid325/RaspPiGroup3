#from rpiHAT.clock import clock
#from rpiHAT.servo import servo
from rpiHAT import RotaryEncoder as Encoder
from rpiHAT import settings as settings
import time

encoder_left = Encoder.Worker(settings.PINS['REV2.3']['encoder0'])
encoder_right = Encoder.Worker(settings.PINS['REV2.3']['encoder1'])
encoder_left.start()
encoder_right.start()

while True:
    print(encoder_left.speed, encoder_right.speed)
    time.sleep(1)


