"""
EXERCÍCIO 064: Tratando Vários Valores v1.0
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""

total = cont = 0
num = int(input('Digite um número [999 para parar]: ')) 

while num != 999:
    total += num
    cont += 1
    num = int(input('Digite um número [999 para papar]: ')) 
    
print(f'A soma dos valores é {total}') 
print(f'Você digitou {cont} números') 
