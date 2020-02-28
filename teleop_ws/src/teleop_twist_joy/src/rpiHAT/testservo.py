#from rpiHAT.clock import clock
#from rpiHAT.servo import servo
from rpiHAT import servo1
from rpiHAT import Clock

t=servo1
t.set(0.1)
clck = Clock(t, 1)
clck.start()

