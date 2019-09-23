"""
EXERCÍCIO 071: Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""

valor = int(input('Quanto quer sacar? R$')) 
total = valor
ced = 50
cont = 0
print('-'*35)
while True:
    
    if total >= ced:
        total -= ced
        cont += 1 
    else:
        if cont > 0:
            print(f'{cont} notas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break
        
print('-'*35)
print('Volte sempre!!') 

"""
#Usando laço for

import os
os.system('clear')
valor = int(input('Quanto quer sacar? R$')) 
print('-'*42)
total = valor
cedulas = [50,20,10,5,2]
for ced in cedulas:
    if total >= ced:
        cont = total // ced
        total = total % ced
        if total < ced:
            print('{:^40}'.format(f'{cont} notas de {ced}')) 
print('-'*42)
print('{:^40}'.format('Volte sempre!')) 
"""
            
            
