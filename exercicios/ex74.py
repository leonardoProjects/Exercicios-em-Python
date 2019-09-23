"""
EXERCÍCIO 074: Maior e Menor Valores em Tupla
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o
maior valor que estão na tupla.
"""

from random import randint
numeros = (randint(0,9),randint(0,9),randint(0,9),
	         randint(0,9),randint(0,9))
print(f'Números gerados: ', end=' ') 
for n in numeros:
    print(n, end=' ')

print(f'\nO número maior é {max(numeros)} e o menor é {min(numeros)}') 
        
