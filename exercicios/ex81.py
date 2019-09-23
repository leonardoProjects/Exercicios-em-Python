"""
EXERCÍCIO 081: Extraindo Dados de uma Lista
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = [] 

while True:
    num = int(input('Digite um número: '))
    lista.append(num) 
    cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    if cont in 'N':
        break

print('~='*20) 
print(f'Foram digitados {len(lista)} números') 
lista.sort(reverse=True)
print(f'lista decrescente: {lista}')

if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 NÃO está na lista.') 