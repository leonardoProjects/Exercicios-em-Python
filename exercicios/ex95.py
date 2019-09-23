"""
EXERCÍCIO 095: Aprimorando os Dicionários
Aprimore o EXERCÍCIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

dados = [] 
while True:
    jogador = {}
    jogador["Nome"] = input('Qual o nome do jogador? ')
    partidas = int(input('Quantas partidas jogou? '))
    jogador["Gols"] = [] 
    dados.append(jogador)
    for i in range(0,partidas):
        jogador["Gols"].append(int(input(f'Quantos gols na {i+1}° partida? '))) 
    jogador["Total"] = sum(jogador["Gols"])
    
    while True:
        cont = input('Quer continuar? [S/N] ').upper().strip()[0]
        if cont in 'SN':
            break
        else:
            print('Por favor digite apenas Sim ou Não.')
    if cont == 'N':
        break

print('-='*20)
print(f'{"Cod.":<5}{"Nome":<10}{"Gols":^10}{"Total":>10}')
print('-'*40)
for pos,j in enumerate(dados):
    print(f'{pos:<5}{j["Nome"]:<13}{j["Gols"]}{j["Total"]:>10}')

cont = 0
while cont != 999:
    print('-='*20) 
    cont = int(input('Mostrar dados de qual jogador? [999 para encerrar] ')) 
    if cont >= 0 and cont < len(dados):
        print('-='*20) 
        print(f'Mostrando levantamento de {dados[cont]["Nome"]}') 
        print('-='*20) 
        for pos,gols in enumerate(dados[cont]["Gols"]):
            print(f'No {pos+1}° jogo fez {gols} gols')         
    else:
        print('Jogador não encontrado!') 
    	
    

