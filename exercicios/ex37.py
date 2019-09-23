"""
DESAFIO 037: Conversor de Bases Numéricas
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""

num = int(input('\033[1;32mDigite um número: '))
print('\033[1;33mEscolha uma base de conversão')
print('1) Para Binário')
print('2) Para Octal')
print('3) Para Hexadecimal')
escolha = int(input('Qual sua escolha?\033[1;32m ')) 
if escolha == 1:
    print('{} em binário é igual a {}'.format(num, bin(num)))
elif escolha == 2:
    print('{} em octal é igual a {}'.format(num, oct(num)))
elif escolha == 3:
    print('{} em hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('\033[37;41mopção inválida!!\033[m') 