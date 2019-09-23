"""
EXERCÍCIO 053: Detector de Palíndromo
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

frase = input('Digite uma frase: ').strip().upper()
junto = frase.split()
palavra = ''.join(frase)
inverso = ''
for letra in range(len(palavra) -1, -1,-1):
    inverso += palavra[letra]

print('O inverso de {} é {}'.format(palavra,inverso))
if inverso == palavra:
    print('Temos um Palindromo')
