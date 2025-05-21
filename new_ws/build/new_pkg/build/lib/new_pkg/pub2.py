import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class FirstPublisher(Node):
    def __init__(self):
        super().__init__("pub1")
        self.publisher_=self.create_publisher(String,'Second_topic',10)
        timer_period=0.5
        self.timer=self.create_timer(timer_period,self.publish_firstpub)
    def publish_firstpub(self):
        msg=String()
        msg.data="Muntaham Shera"
        self.publisher_.publish(msg)
        self.get_logger().info("msg  2 published")
def main(args=None):
    rclpy.init(args=args)
    fp=FirstPublisher()
    rclpy.spin(fp)
if __name__=='__main__':
    main()