import numpy as np


matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]  # Matriz 3x3
print(type(matriz))  # Retorna o tipo da variável
print(matriz)

matriz2 = np.ones((2,3))  # Cria uma matriz 2x3 de uns
print(type(matriz2))
print(matriz2)

matriz3 = np.diag((2,4,6,8,10))
print(type(matriz3))
print(matriz3)