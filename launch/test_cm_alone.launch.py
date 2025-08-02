# In launch/test_cm_alone.launch.py

import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('cruizer_bot')

    # 1. Process the URDF file from the 'description' folder
    xacro_file = os.path.join(pkg_path, 'description', 'robot.urdf.xacro') # <-- FIX IS HERE
    robot_description_config = xacro.process_file(xacro_file)
    robot_description = {'robot_description': robot_description_config.toxml()}

    # 2. Get the path to the controller config file
    controller_config = os.path.join(pkg_path, 'config', 'my_controllers.yaml')

    # 3. Create the controller_manager node
    controller_manager_node = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[robot_description, controller_config],
        output='screen',
    )

    return LaunchDescription([
        controller_manager_node
    ])