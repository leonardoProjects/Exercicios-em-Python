"""
EXERCÍCIO 069: Análise de Dados do Grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""

total = tot18 = totH = totM = 0
cont = 'S'

while cont != 'N':
    idade = int(input('Qual sua idade? '))
    while True:
        sexo = input('Qual o sexo? [M/F]: ').upper().strip()[0] 
        if sexo in 'MF':
            break
            
    if idade < 18:
        tot18 += 1
    
    if sexo == 'M':
        totH += 1
        
    if sexo == 'F' and idade < 20:
        totM += 1
    total += 1
    
    while True:
        cont = input('Quer continuar? [S/N]: ').upper().strip()[0]
        if cont in 'SN':
            break
            
print('-'*35)
print(f'Você cadastrou {total} pessoas.') 
print(f'{tot18} pessoas tem menos de 18 anos.')
print(f'{totH} homens Foram cadastrados.')
print(f'{totM} mulheres tem menos de 20 anos') 
print('-'*35)
      
      
   