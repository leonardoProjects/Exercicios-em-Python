"""
Exercício Python 101: Crie um programa que tenha uma 
função chamada voto() que vai receber como 
parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

from datetime import datetime

def voto(ano_nasc):
    idade = datetime.today().year - ano_nasc
    if idade < 18:
        return f'Com {idade} anos, Não vota!' 
    elif 18 <= idade < 60:
        return f'Com {idade} anos, Voto obrigatório!!' 
    else:
        return f'Com {idade} anos, Voto opcional!' 
        
 
ano_nasc = int(input('Ano de nascimento: ')) 
vota = voto(ano_nasc) 
print(vota) 