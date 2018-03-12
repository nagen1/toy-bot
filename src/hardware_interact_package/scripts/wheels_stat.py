#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32, String

def callback(msg):
    #rospy.loginfo("I hear ya! %s", msg.data)
    pub = rospy.Publisher("wheels_stat", String, queue_size=10)
    pub_stat = msg.data
    
    pub.publish(pub_stat)
    
rospy.init_node('wheels')
sub = rospy.Subscriber("obstacles_distance", String, callback)

rospy.spin()