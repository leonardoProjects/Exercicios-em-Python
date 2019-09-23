"""
EXERCÍCIO 092: Cadastro de Trabalhador em Python
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

pessoa = {} 
pessoa["Nome"] = input('Nome: ') 
pessoa["Nascimento"] = int(input('Ano de nascimento: ')) 
carteira = int(input('Carteira de trabalho: ')) 

ano_atual = date.today().year
idade = ano_atual - pessoa["Nascimento"] 
pessoa["Idade"] = idade

if carteira != 0:
    pessoa["Ctps"] = carteira
    pessoa["Contratacao"] = int(input('Ano de contratação: ')) 
    pessoa["Salario"] = float(input('Salário: ')) 
    pessoa["Aposentadoria"] = pessoa["Contratacao"] - pessoa["Nascimento"] + 35

for k,v in pessoa.items():
    print(f'- {k} => {v}') 
    
