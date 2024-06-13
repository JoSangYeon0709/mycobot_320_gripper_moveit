#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import JointState

def initial_joint_states():
    rospy.init_node('initial_joint_states_publisher')
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)

    # Wait for a short duration to ensure publisher is connected
    rospy.sleep(1.0)

    joint_state = JointState()
    joint_state.header.stamp = rospy.Time.now()
    joint_state.name = ['joint2_to_joint1','joint3_to_joint2','joint4_to_joint3','joint5_to_joint4','joint6_to_joint5','joint6output_to_joint6',
    'gripper_controller','gripper_base_to_gripper_left2','gripper_left3_to_gripper_left1','gripper_base_to_gripper_right3','gripper_base_to_gripper_right2',
    'gripper_right3_to_gripper_right1']
    joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.0, 0.0, 0.0, 0.0, 0.0]

    pub.publish(joint_state)

if __name__ == '__main__':
    try:
        initial_joint_states()
    except rospy.ROSInterruptException:
        pass

