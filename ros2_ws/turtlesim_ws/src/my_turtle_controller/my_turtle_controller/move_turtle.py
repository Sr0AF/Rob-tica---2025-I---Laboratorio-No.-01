import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import termios
import tty
import time
import math

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)  # ejecuta cada 0.1 segundos

    def control_loop(self):
        key = get_key()  # Captura la tecla

        msg = Twist()  # Crea un mensaje vacío

        if key == '\x1b':  # Si es una flecha (escape character)
            key2 = get_key()
            key3 = get_key()

            if key3 == 'A':  # Flecha arriba
                msg.linear.x = 2.0
                msg.angular.z = 0.0
                self.get_logger().info('Avanzando')
            elif key3 == 'B':  # Flecha abajo
                msg.linear.x = -2.0
                msg.angular.z = 0.0
                self.get_logger().info('Retrocediendo')
            elif key3 == 'C':  # Flecha derecha
                msg.linear.x = 0.0
                msg.angular.z = -2.0
                self.get_logger().info('Girando a la derecha')
            elif key3 == 'D':  # Flecha izquierda
                msg.linear.x = 0.0
                msg.angular.z = 2.0
                self.get_logger().info('Girando a la izquierda')

        elif key.lower() == 'a':
            self.draw_A()
        elif key.lower() == 'f':
            self.draw_F()
        elif key.lower() == 'q':
            self.draw_Q()
        elif key.lower() == 'p':
            self.draw_P()
        elif key.lower() == 'm':
            self.draw_M()
        elif key.lower() == 'l':
            self.draw_L()
        elif key.lower() == 'o':
            self.draw_O()
        elif key == 'x':
            self.get_logger().info('Cerrando programa')
            rclpy.shutdown()

        self.publisher_.publish(msg) 

    def wait(self, seconds):
        time.sleep(seconds)

    def stop(self):
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

    def draw_A(self):
        self.get_logger().info('Dibujando A')
        msg = Twist()
        
        # Girar 45°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/4
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar -90°
        msg.linear.x = 0.0
        msg.angular.z = -math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 180°
        msg.linear.x = 0.0
        msg.angular.z = math.pi
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 45°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/4
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 3*math.cos(math.pi/4)
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 45°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/4
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        self.stop()

    def draw_F(self):
        self.get_logger().info('Dibujando F')
        msg = Twist()
        
        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar -90°
        msg.linear.x = 0.0
        msg.angular.z = -math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 180°
        msg.linear.x = 0.0
        msg.angular.z = math.pi
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 180°
        msg.linear.x = 0.0
        msg.angular.z = math.pi
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        self.stop()
    
    def draw_Q(self):
        self.get_logger().info('Dibujando Q')
        msg = Twist()
        
        # Circunferencia
        msg.linear.x = 10.0
        msg.angular.z = 2*math.pi 
        self.publisher_.publish(msg)
        self.wait(1)

        # Arco
        msg.linear.x = 10.0
        msg.angular.z = 2*math.pi
        self.publisher_.publish(msg)
        self.wait(0.125)

        # Giro 90°
        msg.linear.x = 0.0
        msg.angular.z = -math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Giro 180°
        msg.linear.x = 0.0
        msg.angular.z = math.pi
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        self.stop()

    def draw_P(self):
        self.get_logger().info('Dibujando P')
        msg = Twist()

        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar -90°
        msg.linear.x = 0.0
        msg.angular.z = -math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Semicircunferencia
        msg.linear.x = 2.5
        msg.angular.z = -math.pi
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 1.5
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        self.stop()
    
    def draw_M(self):
        self.get_logger().info('Dibujando M')
        msg = Twist()
        
        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar -135°
        msg.linear.x = 0.0
        msg.angular.z = -3*math.pi/4
        self.publisher_.publish(msg)
        self.wait(1)

        # Moverse 
        msg.linear.x = 1.4
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Moverse 
        msg.linear.x = 1.4
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar -90°
        msg.linear.x = 0.0
        msg.angular.z = -3*math.pi/4
        self.publisher_.publish(msg)
        self.wait(1)

        # Bajar recto
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        self.stop()

    def draw_L(self):
        self.get_logger().info('Dibujando L')
        msg = Twist()
        
        # Girar 90°
        msg.linear.x = 0.0
        msg.angular.z = math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Subir recto
        msg.linear.x = 3.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Bajar recto
        msg.linear.x = -3.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        # Girar -90°
        msg.linear.x = 0.0
        msg.angular.z = -math.pi/2
        self.publisher_.publish(msg)
        self.wait(1)

        # Mover recto
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
        self.wait(1)

        self.stop()

    def draw_O(self):
        self.get_logger().info('Dibujando O')
        msg = Twist()
        
        # Hacer circunferencia
        msg.linear.x = 10.0
        msg.angular.z = 2*math.pi
        self.publisher_.publish(msg)
        self.wait(1)

        self.stop()

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()