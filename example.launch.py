from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='rosbridge_server',
            executable='rosbridge_websocket', output='screen'),
        launch_ros.actions.Node(
            package='rosapi',
            executable='rosapi_node', output='screen'),
        launch_ros.actions.Node(
            package='examples_rclpy_minimal_publisher',
            executable='publisher_local_function', output='screen'),

    ])
