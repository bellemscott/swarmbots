#!/usr/bin/env python

# Connect robot tfs to world frame

import rospy
import tf_conversions
import tf2_ros
import geometry_msgs.msg
from nav_msgs.msg import Odometry

def handle_robot_pose(msg, robot_name):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = robot_name + '/map'
    t.transform.translation = msg.pose.pose.position
    t.transform.rotation = msg.pose.pose.orientation

    try:
        trans = tfBuffer.lookup_transform(robot_name + '/odom', robot_name + '/map', rospy.Time())
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
        t.child_frame_id = robot_name + '/odom' # if can't find robot#/map to robot#/odom tf, then connect world to robot#/odom instead
    br.sendTransform(t)

# [INITIALIZE NODE]
rospy.init_node('tf_broadcaster')

tfBuffer = tf2_ros.Buffer()
listener = tf2_ros.TransformListener(tfBuffer)
robot_name = rospy.get_namespace()[1:-1]

rospy.Subscriber('odom',
                     Odometry,
                     handle_robot_pose,
                     robot_name)

# [MAIN CONTROL LOOP]
if __name__ == '__main__':
    rospy.spin()