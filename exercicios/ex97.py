"""
Exercício Python 097: Faça um programa que tenha
uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre 
uma mensagem com tamanho adaptável.
"""
def escreva(msg):
    pos = len(msg)
    print(f'{"~="*pos:^40}')
    print(f'{msg:^40}')
    print(f'{"~="*pos:^40}')

escreva('Oi')