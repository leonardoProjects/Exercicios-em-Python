"""
DESAFIO 040: Aquele Clássico da Média
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(media))
if media >= 7:
    print('Parabéns!! Aprovado!')
elif media >= 5 and media < 7:
    print('Recuperação! ESTUDE MAIS!')
else:
    print('Reprovado! Estude mais ano que vem!') 