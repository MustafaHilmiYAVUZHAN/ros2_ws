#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random
import time

class AnimationPublisher(Node):
    def __init__(self):
        super().__init__('animation_publisher')
        self.pub = self.create_publisher(Int32, '/animation_control', 10)
        self.current_state = False  # Başlangıç durumu False

    def publish_frame(self, frame_number):
        msg = Int32()
        msg.data = frame_number
        self.pub.publish(msg)
        self.get_logger().info(f'▶️ Gönderilen frame numarası: {frame_number}')

    def toggle_state(self):
        # Durumu tersine çevir
        self.current_state = not self.current_state
        self.get_logger().info(f'Durum değişti: {"True" if self.current_state else "False"}')

    def send_frames_in_reverse(self):
        # Durum True olduğunda 59'dan 0'a kadar sayılar gönder
        for frame_number in range(59, -1, -1):
            self.publish_frame(frame_number)
            time.sleep(0.01)  # Her 10 milisaniyede bir gönder

def main(args=None):
    rclpy.init(args=args)
    node = AnimationPublisher()

    try:
        while rclpy.ok():
            # 5 saniyede bir durumu değiştirme olasılığı %50
            time.sleep(5)

            # 50% ihtimalle durum değişikliğine git
            if random.choice([True, False]):
                node.toggle_state()

                # Durum True ise, sayıları 59'dan 0'a gönder
                if node.current_state:
                    node.send_frames_in_reverse()
                else:
                    # Durum False olduğunda başka bir işlem yapabilirsin
                    # Örneğin, 0'dan 59'a kadar sayılar gönder
                    for frame_number in range(0, 60):
                        node.publish_frame(frame_number)
                        time.sleep(0.01)  # Her 10 milisaniyede bir gönder

    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
