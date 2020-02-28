#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import Float32
from sensor_msgs.msg import Joy
speedpub = rospy.Publisher('speed', Float32, queue_size=10)
dirpub = rospy.Publisher('direction', Float32, queue_size=10)
# from rpiHAT import ServoNT

# direction =ServoNT(channel=1, freq=96.5)
# speed = ServoNT(channel=2, freq=96.5)


def scale (unscaledNum, minAllowed, maxAllowed, min, max):
  return (maxAllowed - minAllowed) * (unscaledNum - min) / (max - min) + minAllowed

# def driveCallback(data, args):
#     #check the arugment to pulse to the appropriate channel
#     #data.data is a float32 and the pulse width
#     if args == "direction":
#         direction.pulse(data.data)
#     elif args == "speed":
#         speed.pulse(data.data)
        
    



def callback(data):

    print(data)
    yd = data.axes[1]
    xd = data.axes[0]
    mv = data.buttons[7]
    if mv == 1:
        speedpub.publish(0.13)
    else:
        speedpub.publish(0.15)
    # print(data.buttons[8])
    dirpub.publish(scale(xd,0.1,0.2,-1,1))
    # print(scale(xd,0.1,0.2,-1,1))
    # print(scale(yd,0.1,0.2,-1,1))


def listener():
    rospy.init_node('motor_car', anonymous=True)
    rospy.Subscriber("joy", Joy, callback)
    # rospy.Subscriber('direction', Float32, driveCallback, "direction")
    # rospy.Subscriber('speed', Float32, driveCallback,  "speed")
    while not rospy.is_shutdown():
        time.sleep(0.1)


#START

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

