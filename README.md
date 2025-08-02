Cruizer Bot
Cruizer Bot is a ROS2-based project for simulating a differential drive robot in Ignition Gazebo (Fortress 6.17.0) with ROS2 Humble. The project aims to implement SLAM (Simultaneous Localization and Mapping), teleoperation, and object tracking using ROS2, Nav2, and Rviz. The robot uses ros2_control for hardware interface management and integrates with Gazebo for simulation.
Table of Contents

Features
Prerequisites
Installation
Usage
Directory Structure
Troubleshooting
Contributing
License

Features

Differential drive robot simulation in Ignition Gazebo.
ros2_control integration for joint control and velocity commands.
ROS2-Gazebo bridge for seamless topic communication (e.g., /cmd_vel, /odom, /joint_states).
Support for SLAM, teleoperation, and object tracking (in progress).
Visualization in Rviz for robot state and sensor data.

Prerequisites

OS: Ubuntu 22.04 LTS
ROS2: Humble Hawksbill
Ignition Gazebo: Fortress (6.17.0)
Python: 3.10
Dependencies:
ros-humble-desktop
ros-humble-ros2-control
ros-humble-ros2-controllers
ros-humble-gz-ros2-control
ros-humble-ros-gz
ros-humble-nav2
ros-humble-rviz2



Installation

Install ROS2 Humble:
sudo apt update
sudo apt install ros-humble-desktop
source /opt/ros/humble/setup.bash


Install Ignition Gazebo Fortress:
sudo apt install ignition-fortress


Install ROS2 Control and Gazebo Plugins:
sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-gz-ros2-control ros-humble-ros-gz


Clone the Repository:
mkdir -p ~/dev_ws/src
cd ~/dev_ws/src
git clone https://github.com/muhammed-rafi/cruizer_bot.git


Build the Workspace:
cd ~/dev_ws
colcon build
source install/setup.bash



Usage

Launch the Simulation:Run the simulation in Ignition Gazebo with ros2_control:
ros2 launch cruizer_bot launch_sim.launch.py

This launches:

Ignition Gazebo with test_world.sdf.
Robot state publisher (robot.urdf.xacro).
ros2_control nodes for joint_state_broadcaster and diff_drive_controller.
ROS2-Gazebo bridge for topics like /cmd_vel, /odom, and /joint_states.


Test Teleoperation:Send velocity commands to the robot:
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"


Check ROS2 Control:Verify hardware interfaces:
ros2 control list_hardware_interfaces

Expected output:
command interfaces
    left_wheel_joint/velocity [available]
    right_wheel_joint/velocity [available]
state interfaces
    left_wheel_joint/position [available]
    left_wheel_joint/velocity [available]
    right_wheel_joint/position [available]
    right_wheel_joint/velocity [available]


Visualize in Rviz:Launch Rviz to visualize the robot:
rviz2

Add displays for /odom, /tf, and /scan to monitor the robot’s state.


Directory Structure
cruizer_bot/
├── config/
│   ├── my_controllers.yaml       # ROS2 control configuration
│   ├── gz_bridge.yaml            # ROS2-Gazebo bridge configuration
├── launch/
│   ├── launch_sim.launch.py      # Main simulation launch file
│   ├── rsp.launch.py             # Robot state publisher launch
├── urdf/
│   ├── robot.urdf.xacro          # Robot URDF with ros2_control
├── worlds/
│   ├── test_world.sdf            # Gazebo world file
├── package.xml                   # Package manifest
├── CMakeLists.txt                # Build configuration

Troubleshooting

URDF File Not Found:Ensure robot.urdf.xacro exists in urdf/. Check CMakeLists.txt:
install(
  DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

Rebuild:
colcon build


Controller Manager Not Starting:Verify the controller_manager node:
ros2 node list | grep controller_manager

Check logs:
ros2 topic echo /rosout | grep controller_manager


ros2 control list_hardware_interfaces Timeout:Ensure my_controllers.yaml matches joint names in robot.urdf.xacro. Example:
controller_manager:
  ros__parameters:
    update_rate: 100
    joint_broad:
      type: joint_state_broadcaster/JointStateBroadcaster
    diff_cont:
      type: diff_drive_controller/DiffDriveController
diff_cont:
  ros__parameters:
    left_wheel_names: ["left_wheel_joint"]
    right_wheel_names: ["right_wheel_joint"]


Gazebo Bridge Issues:Verify gz_bridge.yaml bridges necessary topics:
ros2 topic list



Contributing
Contributions are welcome! Please:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
