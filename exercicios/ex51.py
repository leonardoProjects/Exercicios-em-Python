"""
EXERCÍCIO 052: Números Primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

n = int(input('Digite um número: '))
total = 0
for x in range(1,n + 1):
    if n % x == 0:
        total += 1
       
if total == 2:
    print('{} é Primo'.format(n)) 
else:
    print('{} NÃO é primo'.format(n))
    

"""
for x in range(1,101):
    total = 0
    for i in range(1, x+1):
        if x % i == 0:
            total += 1
    if total == 2:
        print(x) 
"""