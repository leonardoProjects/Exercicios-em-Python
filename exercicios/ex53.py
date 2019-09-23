"""
EXERCÍCIO 054: Grupo de Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
from datetime import date

maior = 0
menor = 0
for x in range(1,8):
    ano = int(input('Digite o ano da {} pessoa: '.format(x)))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1
        
print('~=' *21)
print('RESULTADOS') 
print('{} Pessoas são de MAIOR \n{} Pessoas não atingiram a maioridade'.format(maior,menor))
print('~=' *21)
        