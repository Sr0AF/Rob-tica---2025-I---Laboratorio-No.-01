# Robótica 2025-I Laboratorio No. 01 🤖🐢
***Intro a ROS 2 Humble - Turtlesim***  
  
Maria Lucia Arias Ortiz - `mariasor@unal.edu.co`  
Andrés Felipe Quenan Pozo - `aquenan@unal.edu.co`
***

# Diagrama de flujo del controlador de la tortuga

```mermaid
flowchart TD
    A[Inicio: main()] --> B[Inicializar ROS 2]
    B --> C[Crear Nodo TurtleController]
    C --> D[Iniciar hilo para leer teclado]
    D --> E[Spin del Nodo]
    E --> F[Escuchar teclas]

    subgraph TurtleController
        F --> G{Tecla presionada}
        G -->|Flecha arriba| H[Mover hacia adelante]
        G -->|Flecha abajo| I[Mover hacia atrás]
        G -->|Flecha izquierda| J[Girar izquierda]
        G -->|Flecha derecha| K[Girar derecha]
        G -->|Letra A| L[Dibujar letra A]
        G -->|Letra F| M[Dibujar letra F]
        G -->|Letra Q| N[Dibujar letra Q]
        G -->|Letra P| O[Dibujar letra P]
        G -->|Letra M| P[Dibujar letra M]
        G -->|Letra L| Q[Dibujar letra L]
        G -->|Letra O| R[Dibujar letra O]
        G -->|Ctrl+C| S[Terminar programa]
    end

    S --> T[Finalizar Nodo]
    T --> U[Shutdown de ROS 2]
