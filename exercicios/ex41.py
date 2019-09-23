"""
DESAFIO 041: Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    categoria = 'MIRIM'    
elif idade <= 14:
    categoria = 'INFANTIL' 
elif idade <= 19:
    categoria = 'JUNIOR' 
elif idade <= 25:
    categoria = 'SÊNIOR'
elif idade > 25:
    categoria = 'MASTER' 

print('Classificação:', categoria) 
