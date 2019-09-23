"""
EXERCÍCIO 075: Análise de Dados em uma Tupla
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: ')) 
n4 = int(input('Digite o 4° número: ')) 

numeros = (n1, n2, n3, n4) 
print(f'O número 9 aparece {numeros.count(9)} vezes') 

if numeros.count(3):
    print(f'O primeiro valor 3 aparece na {numeros.index(3) + 1}° posição') 
else:
    print('Não existe número três')

print('Os números pares são: ', end='') 

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ') 