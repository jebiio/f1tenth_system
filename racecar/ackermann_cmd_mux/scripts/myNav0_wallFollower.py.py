#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Joy
from ackermann_msgs.msg import AckermannDriveStamped

ack_publisher = None
max_speed = 1 # m/s
max_steering = 1.047198 # radians

pub = rospy.Publisher('high_level/ackermann_cmd_mux/input/nav_0',
                      AckermannDriveStamped, queue_size=1)

def laser_callback(data):
    ack_msg = AckermannDriveStamped()
    ack_msg.header.stamp = rospy.Time.now()
    # ack_msg.header.frame_id = 'your_frame_here'
    ack_msg.drive.steering_angle = 0.1
    ack_msg.drive.speed = 0.0
    pub.publish(ack_msg)
    
if __name__ == '__main__':
    try:
        rospy.init_node('nav_0_wallFollower', anonymous=True)
        rospy.Subscriber("/scan", LaserScan, laser_callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
