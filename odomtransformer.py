#!/usr/bin/env python
import rospy, tf, tf2_ros, geometry_msgs.msg, nav_msgs.msg

def callback(data, args):
	bc = tf2_ros.TransformBroadcaster()
	t = geometry_msgs.msg.TransformStamped()

	t.header.stamp = rospy.Time.now()
	t.header.frame_id = args[0]
	t.child_frame_id = args[1]
	t.transform.translation = data.pose.pose.position
	t.transform.rotation = data.pose.pose.orientation
	
	bc.sendTransform(t)

if __name__ == "__main__":
	rospy.init_node("odomtransformer")
	rospy.Subscriber("/scanmatch_odom", nav_msgs.msg.Odometry, callback, ["/scanmatch_odom", "/base_link"])
	rospy.spin()
