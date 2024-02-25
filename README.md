# Lab1
Reporte de la primer practica de LRT4102 
Python es un lenguaje de programación de alto nivel, interpretado y orientado a objetos, fue diseñado por Guido van Rossum en 1989 con el objetivo de ser un lenguaje fácil de leer y eficiente para el desarrollo de software, es de facil interpretacion ya que el código se ejecuta línea por línea, lo que facilita la depuración y hace que el lenguaje sea ideal para el aprendizaje. 
EJERCICIOS A DESARROLLAR
1. Escribir un programa que lea un entero positivo “n” introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:

\`\`\`python
barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")
\`\`\`


3. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora.Después debe mostrar por pantalla la paga que le corresponde
4. Crea una lista de nombre + sueldo por hora + horas trabajadas de al menos seis operadores.Imprime el nombre y el sueldo a pagar de cada operador.
5. • Crea una lista llamada numeros que contenga al menos 10 números.
   • Calcula el promedio de los números pares y el producto de los números impares.
   • Imprime los resultados.


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

6. Crea un programa que solicite al usuario adivinar un número secreto. El programa debe generarun número aleatorio entre 1 y 10, y el usuario debe intentar adivinarlo. El programa debeproporcionar pistas si el número ingresado por el usuario es demasiado alto o bajo. El bucle whiledebe continuar hasta que el usuario adivine correctamente. Al final se debe imprimir en cuantosintentos el usuario logró adivinar el número.
   Pista:
   import random# Generar un número aleatorio entre 1 y 10
   numero_secreto = random.randint(1, 10)
7. Robot exploradorEl programa debe generar una matriz de al menos 5x5.El robot inicia su camino en la posición (0,0) de la matriz y debe salir en la posición (4,4) o lamáxima posición si se cambia el tamaño de matriz.El numero y la posición de los obstáculos es aleatoria.El robot solo puede avanzar, girar a la izquierda o a la derecha para buscar un camino libre, en eleventual caso que el robot no pueda salir debe imprimir en pantalla “Imposible llegar al destino”En caso de que el robot llegue a su destino final deberá imprimir el mapa, con los espacios libres yobstáculos de la siguiente forma X obstáculo o libre
   
   o o o X o
   
   o o o o o
   
   o o o o X
   
   o o o o o
   
   o X X X o
   
   Deberá imprimir también la ruta que siguió.Mostrar un segundo mapa con el “camino” seguido por el robot mediante flecha
   Pista:
   
   Flecha hacia arriba: ↑ (U+2191)
   
   Flecha hacia abajo: ↓ (U+2193)
   
   Flecha hacia la izquierda: ← (U+2190)
   
   Flecha hacia la derecha: → (U+2192
