# TP1: Algoritmos de Búsqueda en Torre de Hanoi

## Autores
- Marcos Dominguez
- Lucas Monzón
- Felipe Sarche

## Descripción del Proyecto

Este trabajo práctico se centra en la implementación y análisis de algoritmos de búsqueda aplicados al problema clásico de la Torre de Hanoi con 5 discos. El objetivo principal es utilizar el menor número de movimientos posibles para transferir una torre de discos desde una torre inicial a una torre objetivo, respetando las reglas del juego.

## Enunciado del Trabajo

En clase presentamos el problema de la torre de Hanoi. Además, vimos diferentes algoritmos de búsqueda que nos permitieron resolver este problema. Para este trabajo práctico, deberán implementar un método de búsqueda para resolver con 5 discos, del estado inicial y objetivo que se observa en la siguiente imagen:

![Torres Hanoi](https://raw.githubusercontent.com/mrds90/intro_ia/8d7dd6a2f61cad4e3c72f2f85687abdbc869354c/clase2/trabajo_practico_1/torres.png "Torres Hanoi")

## Tareas y Preguntas a Resolver

### 1. ¿Cuáles son los PEAS de este problema?
- **Performance**: Utilizar el menor número de movimientos posibles.
- **Environment**: Discos y torres.
- **Actuators**: Mover discos respetando las reglas del juego.
- **Sensors**: Posición de los discos y estado de las torres.

### 2. ¿Cuáles son las propiedades del entorno de trabajo?
- **Totalmente observable**: Sabemos exactamente todas las posiciones de los discos y el estado de las torres.
- **Determinístico**: Las acciones tienen resultados predecibles.
- **Secuencial**: Cada movimiento de un disco afecta el estado del entorno y las opciones disponibles para los movimientos futuros.
- **Estático**: No hay cambios de estados mientras que el agente no intervenga.
- **Discreto**: Los estados y acciones son finitos y contables.
- **Agente individual**: Solo existe un agente realizando acciones en el entorno.

### 3. Definiciones en el Contexto del Problema
- **Estado**: Ubicación de los discos en las torres en un momento específico.
- **Espacio de estados**: Cantidad de posiciones posibles para los discos en las torres.
- **Árbol de búsqueda**: Representación de los estados posibles y transiciones entre ellos.
- **Nodo de búsqueda**: Un estado específico dentro del árbol de búsqueda.
- **Objetivo**: Configuración en la que todos los discos han sido movidos de la torre inicial a la torre objetivo.
- **Acción**: Mover un disco de una torre a otra, siempre y cuando éste no se apoye sobre un disco más chico.
- **Frontera**: Conjunto de estados que han sido generados pero no explorados.

### 4. Implementación del Método de Búsqueda
Para este trabajo se implementó el algoritmo A* (A estrella) como método de búsqueda para resolver el problema de la Torre de Hanoi.

### 5. Complejidad del Algoritmo
El algoritmo A* tiene una complejidad en tiempo de O(b^d) y en memoria de O(b^d), donde b es el factor de ramificación y d es la profundidad de la solución óptima.

### 6. Evaluación de Performance
Se evaluó el tiempo de ejecución y el uso de memoria del algoritmo implementado. Los resultados se obtuvieron corriendo 10 veces el algoritmo y calculando el promedio y la desviación estándar de las métricas.

### 7. Comparación con la Solución Óptima
La solución óptima para la Torre de Hanoi con 5 discos es de \(2^5 - 1 = 31\) movimientos. Se comparó el número de movimientos realizados por el algoritmo implementado con esta solución óptima.

## Resultados

- **Tiempo de Ejecución Promedio**: 3.29 ms
- **Memoria Promedio Utilizada**: 0.113 MB
- **Número de Movimientos Realizados**: 31
- **Número de Movimientos Óptimos**: 31
- **Diferencia entre el Óptimo y el Implementado**: 0 (0%)

## Instrucciones para Ejecutar el Proyecto

1. Clonar el repositorio del proyecto:
    ```bash
    git clone https://github.com/monzonlucasfabricio/mse-iia.git
    ```
2. Asegúrese de tener todas las dependencias necesarias instaladas. Puede usar el script `setup_env.sh` para generar un entorno virtual para usar como kernel de la notebook.
3. Navegar al directorio del proyecto y ejecutar la notebook o el script principal.

## Enlace al Proyecto

Puede encontrar la implementación completa en la [notebook alojada en el repositorio del proyecto](https://github.com/monzonlucasfabricio/mse-iia/blob/master/HanoiTp/HanoiTP.ipynb).
