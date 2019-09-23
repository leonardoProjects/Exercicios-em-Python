"""
DESAFIO 072: Número por Extenso
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
	         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

cont = ' '
while cont not in 'N':
    while True:
        pos = int(input('Digite um número entre 0 e 20: '))
        if pos >= 0 and pos <= 20:
            break
        print('O número deve ser entre 0 e 20')        
    print(f'Você digitou o número {numeros[pos]}')
    cont = input('Quer continuar? [S/N] ').strip().upper()[0]

print('Volte sempre!') 