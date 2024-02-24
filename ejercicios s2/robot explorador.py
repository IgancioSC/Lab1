import random

def generar_matriz(filas, columnas):
    matriz = [['o' for _ in range(columnas)] for _ in range(filas)]
    return matriz

def colocar_obstaculos(matriz, cantidad_obstaculos):
    for _ in range(cantidad_obstaculos):
        fila = random.randint(0, len(matriz) - 1)
        columna = random.randint(0, len(matriz[0]) - 1)
        matriz[fila][columna] = 'X'
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

def avanzar(matriz, direccion, posicion):
    x, y = posicion

    if direccion == 'arriba' and x > 0 and matriz[x - 1][y] != 'X':
        x -= 1
    elif direccion == 'abajo' and x < len(matriz) - 1 and matriz[x + 1][y] != 'X':
        x += 1
    elif direccion == 'izquierda' and y > 0 and matriz[x][y - 1] != 'X':
        y -= 1
    elif direccion == 'derecha' and y < len(matriz[0]) - 1 and matriz[x][y + 1] != 'X':
        y += 1

    return x, y

def encontrar_camino(matriz):
    camino = []
    direccion = 'derecha'
    posicion = (0, 0)

    while posicion != (len(matriz) - 1, len(matriz[0]) - 1):
        camino.append(posicion)
        if matriz[posicion[0]][posicion[1]] == 'X':
            print("Imposible llegar al destino")
            return None

        if direccion == 'derecha':
            if posicion[1] < len(matriz[0]) - 1 and matriz[posicion[0]][posicion[1] + 1] != 'X':
                posicion = avanzar(matriz, 'derecha', posicion)
            elif posicion[0] > 0 and matriz[posicion[0] - 1][posicion[1]] != 'X':
                direccion = 'arriba'
                posicion = avanzar(matriz, 'arriba', posicion)
            else:
                direccion = 'abajo'
                posicion = avanzar(matriz, 'abajo', posicion)

        elif direccion == 'abajo':
            if posicion[0] < len(matriz) - 1 and matriz[posicion[0] + 1][posicion[1]] != 'X':
                posicion = avanzar(matriz, 'abajo', posicion)
            elif posicion[1] > 0 and matriz[posicion[0]][posicion[1] - 1] != 'X':
                direccion = 'izquierda'
                posicion = avanzar(matriz, 'izquierda', posicion)
            else:
                direccion = 'derecha'
                posicion = avanzar(matriz, 'derecha', posicion)

        elif direccion == 'izquierda':
            if posicion[1] > 0 and matriz[posicion[0]][posicion[1] - 1] != 'X':
                posicion = avanzar(matriz, 'izquierda', posicion)
            elif posicion[0] < len(matriz) - 1 and matriz[posicion[0] + 1][posicion[1]] != 'X':
                direccion = 'abajo'
                posicion = avanzar(matriz, 'abajo', posicion)
            else:
                direccion = 'arriba'
                posicion = avanzar(matriz, 'arriba', posicion)

        elif direccion == 'arriba':
            if posicion[0] > 0 and matriz[posicion[0] - 1][posicion[1]] != 'X':
                posicion = avanzar(matriz, 'arriba', posicion)
            elif posicion[1] < len(matriz[0]) - 1 and matriz[posicion[0]][posicion[1] + 1] != 'X':
                direccion = 'derecha'
                posicion = avanzar(matriz, 'derecha', posicion)
            else:
                direccion = 'izquierda'
                posicion = avanzar(matriz, 'izquierda', posicion)

    camino.append(posicion)
    return camino

def imprimir_camino(matriz, camino):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i, j) in camino:
                print('→', end=' ')
            else:
                print(matriz[i][j], end=' ')
        print()

# Configuración de la matriz
filas = 5
columnas = 5
cantidad_obstaculos = random.randint(5, 10)

# Generar matriz y colocar obstáculos
matriz = generar_matriz(filas, columnas)
colocar_obstaculos(matriz, cantidad_obstaculos)

# Encontrar el camino
camino = encontrar_camino(matriz)

# Imprimir el mapa con obstáculos y espacios libres
print("Mapa con obstáculos y espacios libres:")
imprimir_matriz(matriz)

if camino:
    print("\nCamino seguido por el robot:")
    imprimir_camino(matriz, camino)
    print("\nRuta seguida por el robot:")
    print(" → ".join([f"({pos[0]},{pos[1]})" for pos in camino]))