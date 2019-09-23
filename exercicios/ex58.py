"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0
Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

from random import randint
print('~='*21)
print('Adivinhe o número pensado') 
print('~='*21) 
num = randint(0,10)
acertou = False
errou = 0
while not acertou:
    jogada = int(input('Digite um número: '))
    if num == jogada:
        acertou = True
    else:
        errou += 1
        if num > jogada:
            print('É um número maior...')
        if num < jogada:
            print('É um número menor...')
             
print('Você acertou!!') 
print('Você errou {} vezes'.format(errou))
