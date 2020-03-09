#!/usr/bin/env python


## *** TO PUBLISH TO SUBSCRIBER **
## Copy the command to terminal:
## rostopic pub  /direction std_msgs/Float32 {pulse width (0.1-0.2)}
## OR create your own python script to publish 


#import neccesities 
from rpiHAT import ServoNT
import time
import rospy
from std_msgs.msg import String
import json 
direction =ServoNT(channel=1, freq=96.5)
speed = ServoNT(channel=2, freq=96.5)

def callback(data):
    cardata = json.loads(data.data)
    speed.pulse(cardata["speed"])
    direction.pulse(cardata["direction"])
    
       


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    
    #start the node listener
    rospy.init_node('listener', anonymous=True)
    
    #set up two subscriber topics speed and direction
    #publishing to speed will controll the speed  and 
    #publishing to direction will controll the  car's direction
    
    rospy.Subscriber('cardata', String, callback)

    
    #keep the program running
    rospy.spin()
       

if __name__ == '__main__':
    listener()
