#!/usr/bin/env python

import roslib; roslib.load_manifest('sonar_listener')
import rospy
import math

from std_msgs.msg import *
#from sensor_msgs.msg import LaserScan

def detectSteps(data):

    # Height of step downwards (cm)
    STEP_THRESH = 6

    # Height of sonars from ground 1, 2, 3, 4 (cm)
    SONAR_HEIGHT = [10,10,10,10]

    # Create publisher
    pub = rospy.Publisher('sonar_step_detect', String)

    # Initialise step string
    step = ''
    
    # Loop over the 4 sensor readings. Append 1 if a step is detected
    for i in range(4):
        if data.data[i] > SONAR_HEIGHT[i] + STEP_THRESH:
            step += '1'
        else:
            step += '0'

    pub.publish(step)

def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("sonar", Float32MultiArray, detectSteps)
    rospy.spin()

if __name__ == '__main__':
    main()

