"""
EXERCÍCIO 060: Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

"""
from math import factorial
num = 5
print(factorial(num))

"""
"""
num = int(input('Digite um número: ')) 
fat = 1
for x in range(num,1,-1):
    fat *= x
print('O fatorial de {} é {}'.format(num,fat)) 
"""

"""
n = int(input('Digite um número: ')) 
c = n
fat = 1
while c > 0:
    fat *= c
    c -= 1
print('O fatorial de {} é {}'.format(n, fat))

"""
import os
os.system("ping ...")