#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo(f"Turtle Pose → x: {data.x:.2f}, y: {data.y:.2f}, theta: {data.theta:.2f}")

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
