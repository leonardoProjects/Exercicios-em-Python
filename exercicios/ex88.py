"""
EXERCÍCIO 088: Palpites Para a Mega Sena
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep

num_jogos = int(input('Quantos jogos quer sortear? ')) 
print('-='*20) 
print(f'{"Sorteando jogos":^40}') 
print('-='*20) 
for n in range(1,num_jogos+1):
    numeros = [randint(1,60) for x in range(0,6)]
    sleep(1)
    print(f"Jogo {n}: {numeros}") 
print('-='*20) 