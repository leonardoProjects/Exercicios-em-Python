"""
EXERCÍCIO 090: Dicionário em Python
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

aluno = {}
aluno['nome'] = input('Qual o nome do aluno? ') 
aluno['media'] = float(input('Qual a média? ')) 
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado' 
    
for k,v in aluno.items():
    print(f'{k} => {v}')
