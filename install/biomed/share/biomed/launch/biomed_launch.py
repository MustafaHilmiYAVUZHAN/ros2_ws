from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = get_package_share_directory('biomed')
    urdf_path = os.path.join(pkg_path, 'urdf', 'biomed.urdf')  # URDF dosyasının yolu
    world_path = os.path.join(pkg_path, 'worlds', 'empty.world')  # Dünya dosyasının yolu

    # URDF dosyasını açalım ve içeriğini alalım
    with open(urdf_path, 'r') as urdf_file:
        urdf_content = urdf_file.read()

    # Gazebo ve diğer düğümleri başlatmak için LaunchDescription oluşturuyoruz
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', world_path],
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': urdf_content}]
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'biomed_hand',
                '-topic', 'robot_description',
                # veya '-file', urdf_path
            ],
            output='screen',
            ),
        Node(
            package='biomed',
            executable='mainCode',
            name='mainCode',
            output='screen',
        ),
    ])
