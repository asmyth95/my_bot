import os

from launch import LaunchDescription
from launch_ros.actions import node

def generate_launch_description():


    return LaunchDescription([
        
        Node(
            package='v4l2_camera_node',
            executables='v4l2_camera_node',
            output='screen',
            parameters=[{
                'image_size': [640,480],
                'camera_frame_id': 'camera_link_optical'
                }]
    )
    ])