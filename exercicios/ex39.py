"""
DESAFIO 039: Alistamento Militar
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

ano = int(input('Ano de nascimento: '))
print('''Digite seu sexo
    [ H ] Para Masculino
    [ M ] Para Feminino''') 
sexo = str(input('Sexo: ')) 
atual = date.today().year
idade = atual - ano

if sexo == 'H':
    print('Você tem {} anos'.format(idade))
    if idade < 18:
        saldo = 18 - idade
        print('Falta {} ano(s) para o seu alistamento'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Já passou {} ano(s) do seu alistamento'.format(idade - 18))
        ano = atual - saldo
        print('O alistamento foi em {}'.format(ano))
    else:
        print('Você precisa se alistar IMEDIATAMENTE')
elif sexo == 'M':
    print('Você é mulher e não pode fazer alistamento!')
else:
    print('Opção invalida!!') 