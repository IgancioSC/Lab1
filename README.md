# Lab1
Reporte de la primer practica de LRT4102 
Python es un lenguaje de programación de alto nivel, interpretado y orientado a objetos, fue diseñado por Guido van Rossum en 1989 con el objetivo de ser un lenguaje fácil de leer y eficiente para el desarrollo de software, es de facil interpretacion ya que el código se ejecuta línea por línea, lo que facilita la depuración y hace que el lenguaje sea ideal para el aprendizaje. 
EJERCICIOS A DESARROLLAR 
# PROBLEMA 1
Escribir un programa que lea un entero positivo “n” introducido por el usuario y después muestreen pantalla la suma de todos los enteros desde 1 hasta n . La suma de los primeros enterospositivos puede ser calculada de la siguiente forma:

![image](https://github.com/IgancioSC/Lab1/assets/157633777/5784c93d-953f-4af4-a3e2-826949045b6d)

## Código 1   
```python
 barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
 precio = 3.49 
 descuento = 0.6
 coste = barras * precio * (1 - descuento)

 print("El coste de una barra fresca es " + str(precio) + "€")
 print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
 print("El coste final a pagar es " + str(round(coste, 2)) + "€")
 ```
# Problema 2
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora. Después debe mostrar por pantalla la paga que le corresponde.
## Código 2   
```python
horas = int(input("Introduce el número de horas trabajadas: "))
costo = int(input("Introduce el costo por hora: "))
paga=horas*costo
print("El pago final a pagar es " + str(paga))
```
# Problema 3
## Código 3  
```python
 lista operadores = [
    {"nombre": "Jose", "sueldo_por_hora": 15, "horas_trabajadas": 8},
    {"nombre": "Ivan", "sueldo_por_hora": 20, "horas_trabajadas": 7},
    {"nombre": "Antonio", "sueldo_por_hora": 18, "horas_trabajadas": 9},
    {"nombre": "Ricardo", "sueldo_por_hora": 22, "horas_trabajadas": 6},
    {"nombre": "Daniel", "sueldo_por_hora": 17, "horas_trabajadas": 8},
    {"nombre": "Miguel", "sueldo_por_hora": 19, "horas_trabajadas": 7}
]

# Imprimir el nombre y el sueldo a pagar de cada operador
for operador in lista operadores:
    sueldo_a_pagar = operador["sueldo_por_hora"] * operador["horas_trabajadas"]
    print(f"El sueldo a pagar para {operador['nombre']} es de ${sueldo_a_pagar}")
```
# Problema 4
## Código 4 
```python
```
# Problema 5
## Código 5 
```python
```
# Problema 6
## Código 6  
```python
import random
import numpy as np

# Crear la matriz
size = 5
matrix = np.full((size, size), 'o')

# Colocar obstáculos aleatorios
for _ in range(size):
    i, j = random.randint(0, size-1), random.randint(0, size-1)
    matrix[i][j] = 'X'

# Posición inicial del robot
start = (0, 0)

# Posición final del robot
end = (size-1, size-1)

# Función para encontrar el camino
def find_path(matrix, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    arrows = ['→', '↓', '←', '↑']
    visited = set()
    stack = [(start, [])]
    while stack:
        (x, y), path = stack.pop()
        if (x, y) not in visited:
            visited.add((x, y))
            if (x, y) == end:
                return path
            for (dx, dy), arrow in zip(directions, arrows):
                nx, ny = x + dx, y + dy
                if 0 <= nx < size and 0 <= ny < size and matrix[nx][ny] != 'X':
                    stack.append(((nx, ny), path + [(nx, ny, arrow)]))
    return None

# Encontrar el camino
path = find_path(matrix, start, end)

# Imprimir el resultado
if path is None:
    print("Imposible llegar al destino")
else:
    print("Mapa original:")
    print('\n'.join(' '.join(row) for row in matrix))
    print("Camino seguido:")
    for (x, y, arrow) in path:
        matrix[x][y] = arrow
    print('\n'.join(' '.join(row) for row in matrix))
```
