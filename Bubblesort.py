#algoritmo de ordenação Bubblesort para ordenar um vetor de 10 elementos
import random
def bubble_sort(v):
    final = len(v)
    while final > 0:
        inicio = 0
        while inicio < final - 1:
            if v[inicio] > v[inicio + 1]:
                salvar = v[inicio]
                v[inicio] = v[inicio + 1]
                v[inicio + 1] = salvar
            inicio += 1
        final -= 1
vetor = []

for i in range(0, 10):
    numero = random.randint(0, 101)
    vetor.append(numero)
print(f'Esse é o vetor de 10 elementos aleatórios: \n{vetor}')

bubble_sort(vetor)
print(f'Esse é o vetor organizado pelo algoritmo de ordenação Bubblesort: \n{vetor}')