#!/usr/bin/env python
import rospy
import csv
import sys
from templecar.msg import Drive
from sensor_msgs.msg import Image

def callback(data):
    # This is where we implement the code to control the servos
    rospy.loginfo(rospy.get_caller_id() + "Steering: %d, Speed: %d", data.steering, data.speed)
    speed = data.speed
    steering = data.steering

def callback2(data):
    line_data = [speed, steering]
    for i in data.data:
        line_data.append(ord(i))

    with open(fname,'a') as f:
        writer = csv.writer(f)
        writer.writerow(line_data)

def listener(argv):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('driver', anonymous=True)
    global steering
    global speed
    global fname
    fname = str(argv[0])
    steering = 0.15
    speed = 0.15
    rospy.Subscriber("driving_controls", Drive, callback)
    rospy.Subscriber("/usb_cam/image_raw", Image, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener(sys.argv[1:])
