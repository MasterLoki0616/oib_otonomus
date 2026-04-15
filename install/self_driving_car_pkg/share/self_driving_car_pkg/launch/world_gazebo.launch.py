import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():

    # 1. Paket yolunu alıyoruz
    pkg_share = get_package_share_directory('self_driving_car_pkg')
    
    # 2. .world dosyasının tam yolunu belirtiyoruz
    # Not: src içindeki değil, install içindeki yola bakar, o yüzden path'i böyle kuruyoruz
    world_path = os.path.join(pkg_share, 'worlds', 'sdc.world')

    # 3. gazebo_ros paketindeki gazebo.launch.py dosyasını dahil ediyoruz
    # Bu dosya Gazebo server ve client'ı (GUI) başlatır
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': world_path}.items()
    )

    return LaunchDescription([
        gazebo_launch
    ])