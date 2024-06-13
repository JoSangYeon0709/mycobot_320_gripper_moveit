#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
import rospy
import time
from sensor_msgs.msg import JointState
from std_msgs.msg import Int32
from pymycobot.mycobot import MyCobot


class MyCobotReceiver:
    def __init__(self, port="/dev/ttyACM0", baud=115200):
        rospy.init_node("mycobot_receiver", anonymous=True)
        self.mc = MyCobot(port, baud)
        rospy.sleep(0.05)
        self.mc.set_fresh_mode(1)
        rospy.sleep(0.05)
        self.mc.set_gripper_mode(0)  # 0: 열림, 1: 닫힘
        self.mc.init_eletric_gripper()
        self.mc.set_gripper_calibration()

        self.mc.set_gripper_state(1,20)
        rospy.sleep(2)
        self.mc.set_gripper_state(0,20)
        rospy.sleep(2)
        rospy.Subscriber("joint_states", JointState, self.joint_states_callback)
        
        self.gripper_scale = math.degrees(0.8)

    def joint_states_callback(self, data):
        data_list = []
        for index, value in enumerate(data.position):
            radians_to_angles = round(math.degrees(value), 2)
            data_list.append(radians_to_angles)
        rospy.loginfo("%s", data_list[:7])
        self.mc.send_angles(data_list[:6], 25)
        rospy.sleep(0.05)
        gripper_val=100-min(int(round(data_list[6]/self.gripper_scale*100)),100)
        self.mc.set_gripper_value(gripper_val,30)
    

    def spin(self):
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            rate.sleep()


if __name__ == "__main__":
    receiver = MyCobotReceiver()
    receiver.spin()
