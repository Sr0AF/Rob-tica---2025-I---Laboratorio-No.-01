# Robótica 2025-I Laboratorio No. 01 🤖🐢
***Intro a ROS 2 Humble - Turtlesim***  
  
Maria Lucia Arias Ortiz - `mariasor@unal.edu.co`  
Andrés Felipe Quenan Pozo - `aquenan@unal.edu.co`
***
# Introducción
El presente trabajo tiene como objetivo explorar y aplicar conceptos básicos de control de robots móviles utilizando el simulador Turtlesim en ROS 2. Se desarrolla un nodo que permite controlar el movimiento de una tortuga virtual mediante la lectura de teclas del teclado, enviando comandos de velocidad en tiempo real. Además, se implementa la capacidad de dibujar trayectorias específicas mediante secuencias programadas de movimientos lineales y rotacionales.
Este ejercicio permite afianzar conocimientos sobre el sistema de comunicación de ROS 2, desarrolla habilidades de programación en Python, manipulación de mensajes ROS, y control básico de un robot móvil.

# Objetivos
* Implementar un controlador de teclado en Python que capture entradas en tiempo real y genere comandos de movimiento para la tortuga.
* Programar movimientos básicos de la tortuga en respuesta a las flechas del teclado (avanzar, retroceder, girar a la izquierda y girar a la derecha)
* Diseñar funciones específicas que permitan a la tortuga trazar las letras "A", "F", "Q", "P", "M", "L" y "O" correspondientes a las iniciales de nombres y apellidos de los integrantes, a partir de combinaciones de movimientos lineales y rotacionales.

# Procedimiento
El script `move_controller.py` crea un nodo de ROS2, un publisher que envia mensajes tipo Twist y un timer que llama a la función `control_loop` cada 0.1 segundos, cuando sale de dicha función se destruye el nodo y se termina el programa.  
A continuación se muestra el diagrama de flujo general:
```mermaid
  flowchart TD
    B["Crear nodo"] --> C("Inicializar nodo")
    n1(["Inicio"]) --> B
    n2["Crear publisher"] --> n3["Esperar 0.1 s"]
    C --> n2
    n13["Destruir nodo"] --> n8(["Fin"])
    n3 --> n14["Control loop"]
    n14 --> n13

    B@{ shape: rounded}
    n14@{ shape: subproc}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style B stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style C stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n2 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n3 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n13 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n8 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n14 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```
El procedimiento consta de los siguientes pasos:
## 1. Inicializar nodo:
En la función main se inicia ROS2, luego se crea una instancia del nodo `TurtleController()`, posteriormente el programa entra en un bucle esperando comandos y cuando termina destruye el nodo y apaga ROS2.

```
def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```
## 2. Definir la clase TurtleController:
Se define la clase TurtleController que hereda de Node luego se crea un publisher que publica mensajes Twist en el tópico `/turtle1/cmd_vel.` y por último se crea un timer que cada 0.1 segundos llama a la función `control_loop`.
```
class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)
```
## 3. Función `control_loop` 
Se lee una tecla presionada y se asigna a la variable `key` y se crea un mensaje Twist vacío para configurar el movimiento
```
def control_loop(self):
        key = get_key()
        msg = Twist()
```
Para el movimiento con las flechas la tecla se reconoce como los carácteres `\x1b` seguido de [A para avanzar, de [B para retroceder, de [C para girar a la derecha y de [D para girar a la izquierda. Dependiendo de cada tecla se configura el mensaje Twist con movimiento lineal o rotación para mover la tortuga.
```
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
```
Si la tecla es `a, f, q, p, m, l, o` se llama a la función de dibujo correspondiente.
```
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
```
Si la tecla es `x` se publica el mensaje 'Cerrando programa' y se cierra el nodo.
```
elif key == 'x':
            self.get_logger().info('Cerrando programa')
            rclpy.shutdown()
```
A continuación se muestra el diagrama de flujo de la función:
```mermaid
flowchart TD
    n1(["Inicio"]) --> n2["Capturar tecla"]
    n2 --> n3["Crear mensaje vacío"]
    n3 --> n4["Capturar tecla == flecha?"]
    n4 --- n5["Sí"] & n8["No"]
    n5 --> n6["Hacer trayectoria"]
    n6 --> n7["Configurar y publicar mensaje"]
    n8 --> n9["Capturar tecla == tecla especial?"]
    n9 --- n10["Sí"] & n11["No"]
    n11 --> n12["Capturar tecla == x?"]
    n12 --- n13["Sí"] & n15["No"]
    n13 --> n14["Fin"]
    n15 --> n2
    n10 --> n16["Función de dibujo"]
    n16 --> n17["Configurar y publicar mensaje"]
    n7 --> n2
    n17 --> n2

    n2@{ shape: subproc}
    n4@{ shape: decision}
    n5@{ shape: text}
    n8@{ shape: text}
    n9@{ shape: decision}
    n10@{ shape: text}
    n11@{ shape: text}
    n12@{ shape: decision}
    n13@{ shape: text}
    n15@{ shape: text}
    n14@{ shape: terminal}
    n16@{ shape: subproc}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n2 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n3 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n4 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n6 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n7 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n9 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n12 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n14 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n16 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n17 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```
## 4. Funciones de dibujo
Teniendo en cuenta que la función `linear.x` controla la velocidad lineal, `angular.z` controla la velocidad angular y `self.wait()` controla el tiempo durante el cual se ejecuta los movimientos, se realiza diferentes trazos teniendo en cuenta la posición y orientación de la tortuga en cada tramo para describir las trayectorias. En cada letra a continuación se describe los pasos para construir la trayectoria, estableciendo como tiempo base 1 segundo para cada tramo y considerando que la orientación inicial es hacia la derecha
### Letra A:
```mermaid
flowchart TD
    B@{ label: "<span style=\"padding-left:\">Girar 45°</span>" } --> C("Avanzar 3")
    F("Girar -90°") --> G("Avanzar 3")
    G --> H("Girar 180°")
    n1(["Inicio draw_A"]) --> B
    C --> F
    H --> n2["Avanzar 1.5"]
    n2 --> n3["Girar 45°"]
    n3 --> n4["Avanzar 3*cos(45°)"]
    n4 --> n5["Girar 45°"]
    n5 --> n6["Avanzar 1.5<br>"]
    n6 --> n7["Detener movimiento"]
    n7 --> n8(["Fin draw_A"])

    B@{ shape: rounded}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style B stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style C stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style F stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style G stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style H stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n2 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n3 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n4 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n5 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n6 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n7 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n8 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```
### Letra F:
```mermaid
flowchart TD
    B["Girar 90°"] --> C("Avanzar 3")
    F("Girar -90°") --> G("Avanzar 1.5")
    G --> H("Girar 180°")
    n1(["Inicio draw_F"]) --> B
    C --> F
    H --> n2["Avanzar 1.5"]
    n2 --> n3["Girar 90°"]
    n3 --> n4["Avanzar 1.5"]
    n4 --> n5["Girar 90°"]
    n5 --> n6["Avanzar 1.5<br>"]
    n6 --> n7["Girar 180°"]
    n7 --> n9["Avanzar 1.5"]
    n9 --> n10["Girar 90°"]
    n10 --> n11["Avanzar 1.5"]
    n11 --> n12["Detener movimiento"]
    n12 --> n8(["Fin draw_F"])

    B@{ shape: rounded}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style B stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style C stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style F stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style G stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style H stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n2 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n3 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n4 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n5 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n6 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n7 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n9 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n10 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n11 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n12 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n8 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```
### Letra Q
En este caso para realizar la circunferencia se tiene en cuenta que el tiempo base es 1 segundo, por lo tanto, es necesario una velocidad angular de 2pi rad/s para realizar la circunferencia completa, luego se tomaron las mismas velocidades pero con 1/8 de segundo para trazar 1/8 de circunferencia que corresponde al arco de 45° que recorre la tortuga para posicionarse en donde se hará el trazo final.
```mermaid
flowchart TD
    B["Hacer circunferencia completa"] --> C("Hacer arco de ángulo 45°")
    n1(["Inicio draw_Q"]) --> B
    n2["Girar -90°"] --> n3["Avanzar 1"]
    C --> n2
    n3 --> n9["Girar 180°"]
    n9 --> n10["Avanzar 2"]
    n10 --> n11["Detener movimiento"]
    n11 --> n8(["Fin draw_Q"])

    B@{ shape: rounded}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style B stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style C stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n2 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n3 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n9 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n10 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n11 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n8 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```

### Letra P
```mermaid
flowchart TD
    n6["Girar -90°"] --> n7["Hacer media circunferencia"]
    n1(["Inicio draw_P"]) --> n3["Girar 90°"]
    n3 --> n17["Avanzar 3"]
    n17 --> n6
    n7 --> n18["Girar 90°"]
    n18 --> n19["Avanzar 1.5"]
    n19 --> n20["Detener movimiento"]
    n20 --> n14["Fin draw_P"]

    n14@{ shape: terminal}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style n6 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n7 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n3 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n17 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n18 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n19 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n20 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n14 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```
### Letra M
```mermaid
flowchart TD
    B["Girar 90°"] --> C("Avanzar 3")
    n1(["Inicio draw_"]) --> B
    n2["Girar -135°"] --> n3["Avanzar 1.4"]
    C --> n2
    n3 --> n9["Girar 90°"]
    n9 --> n10["Avanzar 1.4"]
    n10 --> n11["Girar -135°"]
    n11 --> n12["Avanzar 3"]
    n12 --> n13["Detener movimiento"]
    n13 --> n8(["Fin draw_M"])

    B@{ shape: rounded}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style B stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style C stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n2 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n3 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n9 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n10 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n11 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n12 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n13 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n8 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```
### Letra L
```mermaid
flowchart TD
    B["Girar 90°"] --> C("Avanzar 3")
    n1(["Inicio draw_L"]) --> B
    n2["Avanzar 3"] --> n3["Girar -90°"]
    C --> n2
    n3 --> n14["Avanzar 2"]
    n14 --> n15["Detener movimiento"]
    n15 --> n8(["Fin draw_L"])

    B@{ shape: rounded}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style B stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style C stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style n2 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n3 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n14 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n15 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n8 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```
### Letra O
```mermaid
flowchart TD
    n1(["Inicio draw_O"]) --> B["Hacer circunferencia completa"]
    n15["Detener movimiento"] --> n8(["Fin draw_O"])
    B --> n15

    B@{ shape: rounded}
    classDef green fill:#B2DFDB,stroke:#00897B,stroke-width:2px
    classDef orange fill:#FFE0B2,stroke:#FB8C00,stroke-width:2px
    classDef blue fill:#BBDEFB,stroke:#1976D2,stroke-width:2px
    classDef yellow fill:#FFF9C4,stroke:#FBC02D,stroke-width:2px
    classDef pink fill:#F8BBD0,stroke:#C2185B,stroke-width:2px
    classDef purple fill:#E1BEE7,stroke:#8E24AA,stroke-width:2px
    style n1 stroke:#000000,stroke-width:1px,stroke-dasharray: 0
    style B stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n15 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
    style n8 stroke-width:1px,stroke-dasharray: 0,stroke:#000000
```
# Funcionamiento
Para visualizar las trayectorias es necesario compilar el programa mediante los siguientes comandos para un terminal.
```
  cd ros2_ws/turtlesim_ws
  colcon build
  source install/setup.bash
  ros2 run my_turtlesim_controller move_trutle
```
Luego en otro terminal ejecutar:
```
  ros2 run turtlesim turtlesim_node
```
## Flechas:
Desde el primer terminal es posible controlar la tortuga, a continuación se muestra el funcionamiento de las flechas:

