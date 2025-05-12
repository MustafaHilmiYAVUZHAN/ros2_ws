#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class StateSubscriber(Node):
    def __init__(self):
        super().__init__('state_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            '/animation_control',
            self.listener_callback,
            10
        )
        self.current_state = False  # Başlangıçta durumu False kabul ediyoruz

    def listener_callback(self, msg):
        frame_number = msg.data
        if frame_number == 0:
            if not self.current_state:  # Durum False ise True'ya geç
                self.current_state = True
                self.get_logger().info('Durum: True')
        elif frame_number == 59:
            if self.current_state:  # Durum True ise False'ya geç
                self.current_state = False
                self.get_logger().info('Durum: False')

def main(args=None):
    rclpy.init(args=args)
    node = StateSubscriber()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
