#! /usr/bin/env python

#from gpiozero import LED, PWMOutputDevice
from time import sleep
from gpios import gpio40, gpio38, gpio37, gpio36
from std_msgs.msg import Int32, String
import rospy

rospy.init_node("obstacles_distance")
pub = rospy.Publisher('obstacles_distance', String, queue_size=10)

rate = rospy.Rate(10)
obstacles_stat = "going forward"
count = 0

while not rospy.is_shutdown():
    
    if count > 100:
        wheels_stat = "goging backward"
        count = 0
    else:
        count += 1

    pub.publish(obstacles_stat)
    rate.sleep()
