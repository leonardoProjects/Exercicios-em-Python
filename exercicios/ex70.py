"""
EXERCÍCIO 070: Estatísticas em Produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
print('-'*35)
print('Loja Darkmine') 
print('-'*35)

nome = num = menor = total = totM = 0
cont = 'S' 
while cont != 'N':
    nomeP = input('Qual o nome do produto? ')
    preco = int(input('Qual o preço do produto? R$')) 
    total += preco
    num += 1
    if preco >= 1000:
        totM += 1
    
    if num == 1:
        menor = preco
        nome = nomeP
    
    if menor > preco:
        menor = preco
        nome = nomeP
        
    while True:
        cont = input('Deseja continuar? [S/N]: ').upper().strip()[0]
        if cont in 'SN':
            break
    print('-'*35)
    
print('-'*35)
print(f' O total gasto na compra foi R$ {total}') 
print(f' {totM} produtos custam mais de R$ 1000') 
print(f' O produto mais barato foi {nome}') 
print(' Volte sempre!')
print('-'*35)