#!/usr/bin/env python

import roslib; roslib.load_manifest('sonar_listener')
import rospy
import math

from std_msgs.msg import *
from sensor_msgs.msg import LaserScan

def detectSteps(data):

    # Create publisher
    pub = rospy.Publisher('sonar_step_detect', Bool)
   
    # Height of step (cm)
    STEP_THRESH = 10
    if data.data > STEP_THRESH:
        pub.publish(1)
    else:
        pub.publish(0)

def main():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("sonar", Float32, detectSteps)
    rospy.spin()

if __name__ == '__main__':
    main()

