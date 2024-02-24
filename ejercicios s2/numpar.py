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