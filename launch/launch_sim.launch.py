import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node



def generate_launch_description():
    package_name = 'cruizer_bot'

    default_world = os.path.join(
        get_package_share_directory(package_name),
        'worlds',
        'real_test.sdf'
    )

    world = LaunchConfiguration('world')
    use_sim_time = LaunchConfiguration('use_sim_time')

    declare_world_arg = DeclareLaunchArgument(
        'world',
        default_value=default_world,
        description='World to load'
    )

    declare_sim_time_arg = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation time'
    )

    # Robot State Publisher (publishes /robot_description)
    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true', 'use_ros2_control': 'true'}.items()
    )

    # Start Ignition Gazebo (Fortress)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'gz_args': [TextSubstitution(text='-r -v4 '), world],
            'on_exit_shutdown': 'true'
        }.items(),
    )


    # Spawn the robot from /robot_description
    spawn_entity = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                arguments=[
                    '-topic', 'robot_description',
                    '-name', 'my_bot',
                    '-z', '0.1'
                ],
                output='screen'
            )
        ]
    )

    # Controller spawners — Gazebo plugin already provides /controller_manager
    joint_broad_spawner = TimerAction(
        period=8.0,
        actions=[
            Node(
                package='controller_manager',
                executable='spawner',
                arguments=['joint_broad', '--controller-manager', '/controller_manager'],
                output='screen'
            )
        ]
    )

    diff_drive_spawner = TimerAction(
        period=10.0,
        actions=[
            Node(
                package='controller_manager',
                executable='spawner',
                arguments=['diff_cont', '--controller-manager', '/controller_manager'],
                output='screen'
            )
        ]
    )

    # ros_gz bridges
    bridge_params = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'gz_bridge.yaml'
    )

    ros_gz_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=['--ros-args', '-p', f'config_file:={bridge_params}'],
        output='screen'
    )

    ros_gz_image_bridge = Node(
        package="ros_gz_image",
        executable="image_bridge",
        arguments=["/camera/image_raw"],
        output='screen'
    )

    return LaunchDescription([
        declare_world_arg,
        declare_sim_time_arg,
        rsp,
        gazebo,
        spawn_entity,
        joint_broad_spawner,
        diff_drive_spawner,
        ros_gz_bridge,
        ros_gz_image_bridge
    ])
