#o elemento que mais se repete em um vetor de números inteiros

def encontrarElementoMaisRepetido(vetor):
    elementoMaisRepetido = None
    maxRepetiçoes = 0
    for elemento in vetor:
        repeticoes = vetor.count(elemento)
        if repeticoes > maxRepetiçoes:
            maxRepetiçoes = repeticoes
            elementoMaisRepetido = elemento
    return elementoMaisRepetido
print(encontrarElementoMaisRepetido) 
vetor = [10, 2, 10, 3, 9, 2, 79, 54, 40, 40, 40, 45, 42, 40]
elementoMaisRepetido = encontrarElementoMaisRepetido(vetor)
print("O elemento mais repetido é: ", elementoMaisRepetido)