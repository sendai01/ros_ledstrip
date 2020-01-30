#!/usr/bin/env python
import datetime
import rospy
from std_msgs.msg import Int32

rospy.init_node('led_clock')
pub = rospy.Publisher('led_clock_count', Int32, queue_size=1)
rate = rospy.Rate(1)
now = 0
while not rospy.is_shutdown():
	now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
	pub.publish(now.hour)
	rate.sleep()
