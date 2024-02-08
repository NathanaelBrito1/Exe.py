# algoritmo que pede ao usuário 5 números e exiba a soma desses números
soma = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    soma = soma + numero

print("A soma dos números é:", soma)