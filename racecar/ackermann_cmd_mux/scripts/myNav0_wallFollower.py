#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Joy
from ackermann_msgs.msg import AckermannDriveStamped

SPEED = 2.
LIDAR_FREQ = 40
DESIRED_DIST = 0.3

pub = rospy.Publisher('high_level/ackermann_cmd_mux/input/nav_0',
                      AckermannDriveStamped, queue_size=1)

def laser_callback(data):
    
    ranges = data.ranges
    distance_front = ranges[len(ranges)//2]
    distance_side = ranges[len(ranges)//6]
    distance_fonrt_side = ranges[len(ranges)//3]
    alpha = math.atan((distance_fonrt_side*math.cos(math.pi/4)-distance_side) / distance_fonrt_side*math.sin(math.pi/4))
    distance_from_wall = distance_side*math.cos(alpha)
    future_dist_from_wall = distance_from_wall + (SPEED*math.sin(alpha)/LIDAR_FREQ)
    
    error = DESIRED_DIST - future_dist_from_wall

    desired_alpha = error*-0.1
    if desired_alpha > math.radians(10):
        disired_alpha = math.radians(10)
    if desired_alpha < math.radians(-10):
        disired_alpha = math.radians(-10)

    steering_angle = desired_alpha+alpha
    if steering_angle > math.radians(30):
        disired_alpha = math.radians(30)
    if steering_angle < math.radians(-30):
        disired_alpha = math.radians(-30)

    ack_msg = AckermannDriveStamped()
    ack_msg.header.stamp = rospy.Time.now()
    # ack_msg.header.frame_id = 'your_frame_here'
    ack_msg.drive.steering_angle = -steering_angle
    ack_msg.drive.speed = SPEED
    pub.publish(ack_msg)
    
if __name__ == '__main__':
    try:
        rospy.init_node('nav_0_wallFollower', anonymous=True)
        rospy.Subscriber("/scan", LaserScan, laser_callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
