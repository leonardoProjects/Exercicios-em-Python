"""
EXERCÍCIO 067: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    print('-'*35)
    num = int(input('Quer ver a tabuada de qual número? '))
    print('-' *35) 
    
    if num < 0:
        break
    cont = 0
    while cont < 10:
        cont += 1
        print(f'{num} X {cont} = {num*cont}')

print('Programa encerrado!') 