#10 números inteiros e exibir quantos números ímpares foram digitados
impares = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 != 0:
        impares += 1

print("A quantidade de números ímpares digitados é:", impares)