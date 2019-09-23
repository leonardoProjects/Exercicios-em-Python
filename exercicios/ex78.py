"""
EXERCÍCIO 078: Maior e Menor Valores na Lista
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

lista = []
maior = menor = 0

for c in range(0,5):
    lista.append(int(input(f'Digite o {c}° número: ')))
    if c == 0:
        menor = maior = lista[c] 
    else:
        if lista[c] < menor:
            menor = lista[c] 
        if lista[c] > maior:
            maior = lista[c] 
                
print('~='*20) 
print(f'Você digitou os valores: {lista}') 

print(f'O número maior é {maior} nas posições:', end=' ')
for pos,x in enumerate(lista):
    if x == maior:
        print(pos, end='..') 
print() 

print(f'O número menor é {menor} nas posições:', end=' ') 
for pos,x in enumerate(lista):
    if x == menor:
        print(pos, end='..') 
print() 




