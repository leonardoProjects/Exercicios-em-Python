"""
EXERCÍCIO 061: Progressão Aritmética v2.0
Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = 0
while n < 10:
    termo += razao
    print('{} >'.format(termo), end=' ')
    n += 1
print('Fim') 