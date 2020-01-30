#!/usr/bin/env python
import os
import rospy
from std_msgs.msg import Int32

def cb(message):
	n = message.data
	if n > 16:
		os.system('sudo sh -c "echo 0 > /sys/class/gpio/gpio18/value"')
		os.system('sudo sh -c "echo 0 > /sys/class/gpio/gpio23/value"')
		os.system('sudo sh -c "echo 0 > /sys/class/gpio/gpio24/value"')
	else:
		os.system('sudo sh -c "echo 1 > /sys/class/gpio/gpio18/value"')
		os.system('sudo sh -c "echo 1 > /sys/class/gpio/gpio23/value"')
		os.system('sudo sh -c "echo 1 > /sys/class/gpio/gpio24/value"')
	rospy.loginfo(message)

if __name__ == '__main__':
	rospy.init_node('led_control')
	sub = rospy.Subscriber('led_clock_count', Int32, cb)
	rospy.spin()
