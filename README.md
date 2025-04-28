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
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```
## Definir la clase TurtleController:
Se define la clase TurtleController que hereda de Node

```mermaid
---
config:
      theme: redux
---
flowchart TD
        A(["Start"])
        A --> B{"Decision"}
        B --> C["Option A"]
        B --> D["Option B"]

```
