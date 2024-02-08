#programa para encontrar todos os números primos no intervalo de 1 a N, onde N é fornecido pelo usuário
teto = int(input("Digite um teto para a verificação: "))
n = 2

while n < teto: 
    mult = 0
    for count in range (2, n):
        if (n%count == 0):
            mult+=1
    if mult == 0:
        print👎
    n = n + 1