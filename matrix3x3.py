#programa que preencha uma matriz 3x3 com números aleatórios e exiba a soma dos elementos presentes nas colunas ímpares.
import random
matriz = []
somaColuna1 = 0
somaColuna2 = 0

for l in range(3):
    linha = []
    for c in range(3):
        numero = random.randint(1, 101)
        linha.append(numero)
    matriz.append(linha)
print(f'Essa é a Matriz completa: \n{matriz}')
for l in range(0, 3):
    somaColuna1 += matriz [l][0]
print(f'Essa é a soma da primeira coluna (coluna ímpar): \n{somaColuna1}')
for l in range(0, 3):
    somaColuna2 += matriz [l][2]
print(f'Essa é a soma da terceira coluna (coluna ímpar): \n{somaColuna2}')