#programa que exiba os números primos de 1 a 100
n = 2

while n < 101: 
    mult = 0
    for count in range (2, n):
        if (n%count == 0):
            mult+=1
    if mult == 0:
        print👎
    n = n + 1