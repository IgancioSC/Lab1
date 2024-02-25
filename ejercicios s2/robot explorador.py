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
