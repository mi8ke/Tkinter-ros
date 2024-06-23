import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def launch_turtlebot3_gazebo():
    command = "ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py"
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

def launch_turtlebot3_navigation2():
    home_dir = os.path.expanduser("~")
    command = f"ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:={home_dir}/map.yaml"
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

def launch_rviz2():
    rviz_file_path = filedialog.askopenfilename(
        title="Select RViz Config File",
        filetypes=[("RViz Config Files", "*.rviz"), ("All Files", "*.*")]
    )
    if rviz_file_path:
        command = f"rviz2 -d {rviz_file_path}"
        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

def colcon_build():
    command = "cd ~/ros2_ws && colcon build --symlink-install; exec bash"
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])

app = tk.Tk()
app.title("ROS 2 Launcher")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

gazebo_button = tk.Button(frame, text="Launch Turtlebot3 Gazebo", command=launch_turtlebot3_gazebo)
gazebo_button.pack(pady=5)

navigation_button = tk.Button(frame, text="Launch Turtlebot3 Navigation2", command=launch_turtlebot3_navigation2)
navigation_button.pack(pady=5)

rviz_button = tk.Button(frame, text="Launch RViz2", command=launch_rviz2)
rviz_button.pack(pady=5)

rviz_button = tk.Button(frame, text="colcon build", command=colcon_build)
rviz_button.pack(pady=5)

app.mainloop()
