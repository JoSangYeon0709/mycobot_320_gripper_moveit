mycobot320 moveit 수정본

기존에있는 mycobot_ros는 삭제


로봇암 + 그리퍼 경우
터미널1
roslaunch mycobot_320_gripper_moveit mycobot_320_gripper_moveit.launch
터미널2
rosrun mycobot_320_gripper_moveit sync_plan.py


로봇암 + cam + 그리퍼 경우
터미널1
roslaunch mycobot_320_cam_gripper_moveit mycobot_320_cam_gripper_moveit.launch
터미널2
rosrun mycobot_320_cam_gripper_moveit sync_plan.py


단순히 rviz에서 확인시
터미널
roslaunch mycobot_description display.launch

display_cam_gripper.launch
display_gripper.launch
하면 됨

터미널2에서 포트 못 여는 에러시 chmod +777 /dev/ttyACM0

가제보 수정안했음. 사용 ㄴㄴ

에러 발견시 문의
whtkddus159@naver.com

마지막 수정 2024.06.03
