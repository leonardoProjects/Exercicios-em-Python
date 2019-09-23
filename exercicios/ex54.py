"""
EXERCÍCIO 055: Maior e Menor da Sequência
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = 0
for i in range(1,6):
    peso = int(input('Digite o peso da {}° pessoa: '.format(i))) 

    if peso > maior:
        maior = peso
    if i == 1:
        menor = peso
    if peso < menor:
        menor = peso
        
print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))