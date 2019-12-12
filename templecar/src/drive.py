#!/usr/bin/python

import rospy
from std_msgs.msg import Float32
from beginner_tutorials.msg import Num
import keyboard
import time


def wCallback(e):
    global speed
    print('w')

    if keyboard.is_pressed('s'):
        speed = .15
        return

    if e.event_type == "down":
        speed = .19
    elif e.event_type == "up":
        speed = .15

    return


def sCallback(e):
    global speed
    print('s')

    if keyboard.is_pressed('w'):
        speed = .15
        return

    if e.event_type == "down":
        speed = .11
    elif e.event_type == "up":
        speed = .15

    return


def dCallback(e):
    global steering
    print('d')

    if keyboard.is_pressed('a'):
        steering = .15
        return

    if e.event_type == "down":
        steering = .19
    elif e.event_type == "up":
        steering = .15
    return


def aCallback(e):
    global steering
    print('a')

    if keyboard.is_pressed('d'):
        steering = .15
        return

    if e.event_type == "down":
        steering = .11
    elif e.event_type == "up":
        steering = .15

    return

def talker():
    global pub
    global speed
    global steering
    rospy.init_node('talker', anonymous=True, disable_signals=True)
    rate = rospy.Rate(10)  # 10hz
    msg = Num()
    keyboard.hook_key('w', wCallback)
    keyboard.hook_key('s', sCallback)
    keyboard.hook_key('a', aCallback)
    keyboard.hook_key('d', dCallback)
    while not rospy.is_shutdown():
        msg.speed = speed
        msg.steering = steering
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    pub = rospy.Publisher('Car', Num, queue_size=1)
    speed = .15
    steering = .15
    try:
        talker()
    except KeyboardInterrupt:
        msg = Num()
        msg.speed = .15
        msg.steering = .15
        print("interupting")
        pub.publish(msg)