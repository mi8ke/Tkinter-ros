import tkinter as tk
import subprocess
import os

def launch_turtlebot3_gazebo():
    command = "ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py"
    subprocess.Popen(command, shell=True)

def launch_turtlebot3_navigation2():
    home_dir = os.path.expanduser("~")
    command = f"ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:={home_dir}/map.yaml"
    subprocess.Popen(command, shell=True)

app = tk.Tk()
app.title("ROS 2 Launcher")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

gazebo_button = tk.Button(frame, text="Launch Turtlebot3 Gazebo", command=launch_turtlebot3_gazebo)
gazebo_button.pack(pady=5)

navigation_button = tk.Button(frame, text="Launch Turtlebot3 Navigation2", command=launch_turtlebot3_navigation2)
navigation_button.pack(pady=5)

app.mainloop()
