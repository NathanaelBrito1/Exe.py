#recebendo do usuário 10 números, armazenando em um vetor e exibindo a média dos valores pares
vetor = []
vetorPar = []

for i in range(10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)
    if numero %2 == 0:
        vetorPar.append(numero)
soma = sum(vetorPar)/2
print(f'Esse é o vetor com numeros pares: {vetorPar} e esse é a média dos valores pares: {soma}')