"""
EXERCÍCIO 080: Lista Ordenada sem Repetições
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

lista = []

for x in range(0,5):
    num = int(input('Digite um número: ')) 
    if x == 0 or num > lista[-1]:
        lista.append(num)
    else:
        for pos,i in enumerate(lista):
            if num <= i:
                lista.insert(pos, num) 
                break        
print(f'Os números em ordem crescente são: {lista}') 