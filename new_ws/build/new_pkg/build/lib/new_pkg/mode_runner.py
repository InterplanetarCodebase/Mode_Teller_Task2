import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ModeMonitor(Node):
    def __init__(self):
        super().__init__('mode_monitor')
        self.status_pub = self.create_publisher(String, 'mode_status', 10)
        self.timer = self.create_timer(1.0, self.check_nodes)

    def check_nodes(self):
        node_names = self.get_node_names()
        msg = String()

        auto_running = 'pub1' in node_names
        manual_running = 'pub2' in node_names

        if auto_running and manual_running:
            msg.data = 'Running in both Autonomous and Manual'
        elif auto_running:
            msg.data = 'Running in Autonomous'
        elif manual_running:
            msg.data = 'Running in Manual'
        else:
            msg.data = 'No control node running'

        self.status_pub.publish(msg)
        self.get_logger().info(f'Published status: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ModeMonitor()
    rclpy.spin(node)
    

if __name__ == '__main__':
    main()
