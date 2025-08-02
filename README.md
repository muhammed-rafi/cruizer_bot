# 🚀 Cruizer Bot

![ROS Version](https://img.shields.io/badge/ROS-Humble-blue) ![Gazebo Version](https://img.shields.io/badge/Gazebo-Fortress-orange)

This repository contains the simulation setup for **Cruizer Bot** using **ROS 2 Humble**, **Gazebo Fortress**, and **ros2_control**. The simulation includes hardware interface integration, controller configuration, and joint state broadcasting.

---

## 🛠 Features

- ROS 2 Humble-based simulation environment
- Differential drive robot with `ros2_control`
- Integration with Gazebo Fortress via `gz_ros2_control`
- Sensor and camera plugin simulation
- Launch files to spawn the robot and load controllers
- Live publishing of `/joint_states` and `/odom`

---

## 🔧 Dependencies

Make sure the following packages are installed:

```bash
sudo apt update && sudo apt install \
  ros-humble-xacro \
  ros-humble-ros2-control \
  ros-humble-ros2-controllers \
  ros-humble-joint-state-broadcaster \
  ros-humble-diff-drive-controller \
  ros-humble-controller-manager \
  ros-humble-gz-ros2-control \
  ros-humble-gz-ros2-control-demos \
  ros-humble-gazebo-ros \
  ros-humble-gazebo-ros-pkgs
```

---

## ⚙️ Installation

1.  **Clone the Repository:**
    ```bash
    mkdir -p ~/dev_ws/src
    cd ~/dev_ws/src
    git clone [https://github.com/muhammed-rafi/cruizer_bot.git](https://github.com/muhammed-rafi/cruizer_bot.git)
    ```

2.  **Build the Workspace:**
    ```bash
    cd ~/dev_ws
    colcon build
    source install/setup.bash
    ```

---

## ▶️ Usage

### 1. Launch the Simulation
Run the main launch file to start Gazebo, spawn the robot, and load the controllers:
```bash
ros2 launch cruizer_bot launch_sim.launch.py
```


## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.
