#!/usr/bin/env python
import rospy
import  json
from datetime import datetime
import time
from std_msgs.msg import String
from sensor_msgs.msg import Joy
import pandas as pd
pub = rospy.Publisher('cardata', String, queue_size=10)
temp = {"speed":0.15,"direction":0.15}
csv = {"speed":[],"direction":[],"time":[]}
df = pd.DataFrame(csv)
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

    #print(data)
    yd = data.axes[1]
    xd = data.axes[0]
    mv = data.buttons[7]
    dataObj = {}
    if mv == 1:
        dataObj["speed"] = 0.13
    else:
        dataObj["speed"] = 0.15
    dataObj["direction"] = scale(xd,0.1,0.2,-1,1) 
    
    if dataObj["speed"] != temp["speed"] or dataObj["direction"] != temp["direction"]:
        #send data
        pub.publish(json.dumps(dataObj))
        global df
        df = df.append({"speed":dataObj["speed"], "direction":dataObj["direction"],"time":str(datetime.now())},ignore_index=True)
        df.to_csv("out.csv",index=False)



    global temp # do not delete because it breaks :( everythigng
    temp = dataObj

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

