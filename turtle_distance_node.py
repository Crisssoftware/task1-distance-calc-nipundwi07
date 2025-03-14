import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math
class TurtleDistanceNode(Node):
    def __init__(self):
        super().__init__('turtle_distance_node')
        
        # Subscriber to /turtle1/pose
        self.pose_subscription = self.create_subscription(Pose,'/turtle1/pose',
            self.pose_callback,
            10
        ) 
        # Publisher to /turtle1/distance_from_origin
        self.distance_publisher = self.create_publisher(
            Float32,
            '/turtle1/distance_from_origin',
            10)
    def pose_callback(self, msg: Pose):
        # Extract x, y from the message
        x = msg.x
        y = msg.y
        
        # Compute the distance from the origin (0, 0)
        distance = math.sqrt(x ** 2 + y ** 2)
        
        # Create a message to publish the distance
        distance_msg = Float32()
        distance_msg.data = distance
         # Publish the computed distance
        self.distance_publisher.publish(distance_msg)
        self.get_logger().info(f'Distance from origin: {distance}')

def main(args=None):
    rclpy.init(args=args)
    turtle_distance_node = TurtleDistanceNode()

    rclpy.spin(turtle_distance_node)

    turtle_distance_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()