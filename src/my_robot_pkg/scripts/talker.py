#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def main():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        rospy.loginfo(f"Publishing: linear.x = {msg.linear.x}, angular.z = {msg.angular.z}")
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    main()

