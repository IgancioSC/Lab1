# Lab1
Reporte de la primer practica de LRT4102 

Python es un lenguaje de programación de alto nivel, interpretado y orientado a objetos, fue diseñado por Guido van Rossum en 1989 con el objetivo de ser un lenguaje fácil de leer y eficiente para el desarrollo de software, es de facil interpretacion ya que el código se ejecuta línea por línea, lo que facilita la depuración y hace que el lenguaje sea ideal para el aprendizaje. 

EJERCICIOS A DESARROLLAR 
# PROBLEMA 1
Escribir un programa que lea un entero positivo “n” introducido por el usuario y después muestreen pantalla la suma de todos los enteros desde 1 hasta n . La suma de los primeros enterospositivos puede ser calculada de la siguiente forma:

![image](https://github.com/IgancioSC/Lab1/assets/157633777/5784c93d-953f-4af4-a3e2-826949045b6d)

## Código 1   
```python
#pide las barras vendidas introducir un numero cualquiera
barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
#datos de los productos
 precio = 3.49 
 descuento = 0.6
#calcula el costo multiplicando las barras vendidas por su precio aplicando el descuento y almacena la variable
 coste = barras * precio * (1 - descuento)
#imprime los costos dependiendo si es una barra fresca o no y el costo final
 print("El coste de una barra fresca es " + str(precio) + "€")
 print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
 print("El coste final a pagar es " + str(round(coste, 2)) + "€")
 ```
# Problema 2
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora. Después debe mostrar por pantalla la paga que le corresponde.
## Código 2   
```python
#se coloca mumero de horas trabajadas, cualquier numero.Usamos int convirtiendolo en un intero y almacena la variable en horas
horas = int(input("Introduce el número de horas trabajadas: "))
#agrega el precio que se paga por hora ahora guardamos la variable en costo
costo = int(input("Introduce el costo por hora: "))
#calculamos la paga con una multiplicacion
paga=horas*costo
#imprime la paga final y str(paga) convierte el valor numerico para concatenarse con otras cadenas
print("El pago final a pagar es " + str(paga))
```
# Problema 3
Crea una lista de nombre + sueldo por hora + horas trabajadas de al menos seis operadores.Imprime el nombre y el sueldo a pagar de cada operador.
## Código 3  
```python
#se ingresan los datos de operadores, horas que trabajan y cuanto ganan por hora.
 operadores = [
    {"nombre": "Jose", "sueldo_por_hora": 15, "horas_trabajadas": 8},
    {"nombre": "Ivan", "sueldo_por_hora": 20, "horas_trabajadas": 7},
    {"nombre": "Antonio", "sueldo_por_hora": 18, "horas_trabajadas": 9},
    {"nombre": "Ricardo", "sueldo_por_hora": 22, "horas_trabajadas": 6},
    {"nombre": "Daniel", "sueldo_por_hora": 17, "horas_trabajadas": 8},
    {"nombre": "Miguel", "sueldo_por_hora": 19, "horas_trabajadas": 7}
]

# Imprimir el nombre y el sueldo a pagar de cada operador
for operador in operadores:
    sueldo_a_pagar = operador["sueldo_por_hora"] * operador["horas_trabajadas"]
    print(f"El sueldo a pagar para {operador['nombre']} es de ${sueldo_a_pagar}")
```
# Problema 4
• Crea una lista llamada numeros que contenga al menos 10 números.

• Calcula el promedio de los números pares y el producto de los números impares.

• Imprime los resultados.
## Código 4 
```python
# Crear una lista de números
numeros = [10, 22, 5, 7, 29, 8, 13, 2, 17, 19]

# Inicializar variables para el promedio de los números pares y el producto de los números impares
suma_pares = 0
cont_pares = 0
producto_impares = 1

# Iterar sobre la lista de números
for num in numeros:
    if num % 2 == 0:  # Si el número es par
        suma_pares += num
        cont_pares += 1
    else:  # Si el número es impar
        producto_impares *= num

# Calcular el promedio de los números pares
promedio_pares = suma_pares / cont_pares if cont_pares > 0 else 0

# Imprimir los resultados
print(f"El promedio de los números pares es {promedio_pares}")
print(f"El producto de los números impares es {producto_impares}")
```
# Problema 5
Crea un programa que solicite al usuario adivinar un número secreto. El programa debe generarun número aleatorio entre 1 y 10, y el usuario debe intentar adivinarlo. El programa debeproporcionar pistas si el número ingresado por el usuario es demasiado alto o bajo. El bucle whiledebe continuar hasta que el usuario adivine correctamente. Al final se debe imprimir en cuantosintentos el usuario logró adivinar el número.

pista: 

import random

Generar un número aleatorio entre 1 y 10

numero_secreto = random.randint(1, 10)

## Código 5 
```python
import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

intentos = 0 #para ver cuantos intentos se realizan al adivinar el numero

#bucle infinito
while True:
    numero_usuario = int(input("Adivina el número secreto entre 1 y 10: ")) #introducir un  numero y convertios a un entero con int y lo almacenamos en "num_usuario"
    intentos += 1 #contador, agrega los intentos

#compara el numero dado y envia un mensaje dependiendo si el numero es muy grande o pequeño o es el correcto
    if numero_usuario < numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    elif numero_usuario > numero_secreto:
        print("Demasiado alto, intenta de nuevo.")
    else:
        print(f"¡Bien hecho! Has adivinado el número secreto en {intentos} intentos.")
        break #para romper el bucle infinito y terminar el juego
```
# Problema 6
Robot exploradorEl programa debe generar una matriz de al menos 5x5.El robot inicia su camino en la posición (0,0) de la matriz y debe salir en la posición (4,4) o lamáxima posición si se cambia el tamaño de matriz.El numero y la posición de los obstáculos es aleatoria.El robot solo puede avanzar, girar a la izquierda o a la derecha para buscar un camino libre, en eleventual caso que el robot no pueda salir debe imprimir en pantalla “Imposible llegar al destino”En caso de que el robot llegue a su destino final deberá imprimir el mapa, con los espacios libres yobstáculos de la siguiente forma X obstáculo o libre

o o o X o

o o o o o

o o o o X

o o o o o

o X X X o

Deberá imprimir también la ruta que siguió.

Mostrar un segundo mapa con el “camino” seguido por el robot mediante flechas

pista: 

Flecha hacia arriba: ↑ (U+2191)

Flecha hacia abajo: ↓ (U+2193)

Flecha hacia la izquierda: ← (U+2190)

Flecha hacia la derecha: → (U+2192)
## Código 6  
```python
#librerias donde random=numeros aleatorios y numpy=operaciones matriciales 
import random
import numpy as np

# Crear la matriz cuadrada de 5*5 y con np.full llena el caracter "o"
size = 5
matrix = np.full((size, size), 'o')

# bucle para colocar obstáculos aleatorios
for _ in range(size):
    i, j = random.randint(0, size-1), random.randint(0, size-1) #genera cordenadas aleatorias
    matrix[i][j] = 'X' #es para colocar un obstaculo y tapar el camino

# Posición inicial del robot comenzando por la esquina derecha de arriba
start = (0, 0)

# Posición final del robot en la esquina derecha de abajo
end = (size-1, size-1)

# para encontrar el camino usamos find_path tomando la matriz con la posicion inicial y final dando los pasos que toma el robot 
def find_path(matrix, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    arrows = ['→', '↓', '←', '↑']
    visited = set() #para marcar las celdas donde pasa el robot
    stack = [(start, [])] #crea una lista con la posicion inicial y una lista vacia para ver el camino recorrido
#bluqcle que sirve para ejecutarse mientras tengamos algun elemento 
while stack:
        (x, y), path = stack.pop() #muestra la poscicion y el camino desde el principio
        if (x, y) not in visited:#para confirmar si la poscicion actual no se ha visitado
            visited.add((x, y)) #agrega poscicion actual a las visitadas
            if (x, y) == end:#verifica si el robot a llegado al final
                return path #devuelve el camino recorrido para ver si a llegado a la poscicion final
            for (dx, dy), arrow in zip(directions, arrows):#verifica las direcciones posibles y flechas asociadas
                nx, ny = x + dx, y + dy #calcula las nuevas cordenadas segun la direccion dada
                if 0 <= nx < size and 0 <= ny < size and matrix[nx][ny] != 'X': #verifica si las nuevas cordenadas estan en la matriz y si hay o no obstaculos
                    stack.append(((nx, ny), path + [(nx, ny, arrow)]))#agrega las nuevas cordenadas 
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
