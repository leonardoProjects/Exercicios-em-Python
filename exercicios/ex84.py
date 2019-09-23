"""
EXERCÍCIO 084: Lista Composta e Análise de Dados
Faça um programa que leia nome e peso de várias 
pessoas, guardando tudo em uma lista. 
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

lista = []

while True:
    print('-='*20)
    nome = input('Digite o nome: ')
    peso = float(input('Digite a idade: '))
    lista.append([nome, peso])
    cont = input('Deseja continuar cadastrando? [S/N] ').strip().upper()[0]
    if cont in 'N':
        break
        
print('-='*20) 
print(f'Foram cadastradas {len(lista)} pessoa') 
print('-='*20) 
print('As pessoas mais leves são:') 
for x in lista:
    if x[1] <= 80:
        print(f'{x[0]} tem {x[1]}Kg')
print('-='*20)
print('As pessoas mais pesadas são:') 
for x in lista:
    if x[1] > 80:
        print(f'{x[0]} com {x[1]}Kg')
print('-='*20) 



