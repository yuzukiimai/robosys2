#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
def cb(message):
    global n
    n = message.data
rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('twice', Int32, queue_size=1)
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    if n % 3 == 0  and n != 0:
        print('ナベアツ「%d ↑↑」\n' % n)
     
    pub.publish(n)
    rate.sleep()
