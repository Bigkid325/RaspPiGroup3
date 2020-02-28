from threading import Timer,Thread,Event
from time import sleep

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.5):
            print("my thread")

stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()
thread2 = MyThread(stopFlag)
thread2.start()
# this will stop the timer
sleep(2)
stopFlag.set()
