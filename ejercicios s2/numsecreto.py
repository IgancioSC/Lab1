import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

intentos = 0

while True:
    numero_usuario = int(input("Adivina el número secreto entre 1 y 10: "))
    intentos += 1

    if numero_usuario < numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    elif numero_usuario > numero_secreto:
        print("Demasiado alto, intenta de nuevo.")
    else:
        print(f"¡Bien hecho! Has adivinado el número secreto en {intentos} intentos.")
        break