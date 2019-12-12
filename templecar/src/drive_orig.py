#!/usr/bin/python

import rospy
from std_msgs.msg import Float32
from beginner_tutorials.msg import Num
import sys

def talker(s,t):
    global pub
    global speed
    global steering
    rospy.init_node('talker', anonymous=True, disable_signals=True)
    rate = rospy.Rate(10)  # 10hz
    msg = Num()
    while not rospy.is_shutdown():
        msg.speed = s
        msg.steering = t
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    pub = rospy.Publisher('Car', Num, queue_size=1)
    try:
        talker(float(sys.argv[1]), float(sys.argv[2]))
    except KeyboardInterrupt:
        msg = Num()
        msg.speed = .15
        msg.steering = .15
        print("interupting")
        pub.publish(msg)