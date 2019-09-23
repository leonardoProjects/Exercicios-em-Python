"""
EXERCÍCIO 076: Lista de Preços com Tupla
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

listagem = ('Lápis', 1.75,
           'caneta', 2,
           'caderno', 20,
           'Borracha', 3,
           'Notebook', 1234,
           'Celular', 756,
           'mouse', 56)
print('-'*42)
print(f'{"Listagem de produtos":^40}')
print('-'*42)

for x in range(0,len(listagem)):
    if x % 2 == 0:
        print(f'{listagem[x]:.<20}', end=' ')
    else:
        print(f'Preço R$ {listagem[x]:.2f}')

print('-'*42)