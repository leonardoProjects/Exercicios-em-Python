"""
EXERCÍCIO 093: Cadastro de Jogador de Futebol
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = {}
jogador["Nome"] = input('Qual o nome do jogador? ')
partidas = int(input('Quantas partidas jogou? '))
jogador["Gols"] = [] 
for i in range(0,partidas):
    jogador["Gols"].append(int(input(f'Quantos gols na {i+1}° partida? '))) 
jogador["Total"] = sum(jogador["Gols"])
print('-='*20)
print(jogador)
print('-='*20)

for k,v in jogador.items():
    print(f' - {k} tem valor {v}')
print('-='*20)

for pos,v in enumerate(jogador["Gols"]):
    print(f' - Partida {pos+1} fez {v} gols') 
