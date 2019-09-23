"""
EXERCÍCIO 091: Jogo de Dados em Python
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint 
from time import sleep
from operator import itemgetter

jogadores = {}
print('-=' *20)
print(f'{"Sorteando jogadores":^40}') 
for j in range(1,5):
    jogadores[f'Jogador {j}'] = randint(1,6)

print('-='*20) 
for k,v in jogadores.items():
    print(f'{k} tirou: {v}')
    sleep(0.5)
print('-='*20) 

ranking = sorted(jogadores.items(),key = itemgetter(1), reverse=True)

print(f'{"Ranking dos jogadores":~^40}')
print('-='*20) 
for pos, v in enumerate(ranking):
    print(f'  {pos+1}° Lugar: {v[0]} com {v[1]}.') 
    sleep(0.5)
    

