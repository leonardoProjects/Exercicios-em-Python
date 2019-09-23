"""
EXERCÍCIO 087: Mais Sobre Matriz em Python
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
"""

line = int(input('Quantas linhas tem a Matriz? ')) 
column = int(input('Quantas colunas tem a matriz? ')) 
matriz = [[] for x in range(0,line)]

for i in range(0, line):
    for j in range(0, column):
        matriz[i].append(int(input(f'Digite [ a{i+1}{j+1} ]: '))) 
        
print('\nMatriz: ') 
soma_pares = soma_column3 = maior = 0

for a in matriz:
    for pos,num in enumerate(a):
        if num % 2 == 0:
            soma_pares += num
            
        if pos == 2:
            soma_column3 += num
        print(f'[ {num:^5} ]', end='  ') 
    print()     
print(f'A soma dos pares é: {soma_pares}')
if column >= 3:
    print(f'A soma da terceira coluna é {soma_column3}') 
if line >= 2:
    maior = max(matriz[1])
    print(f'O maior valor da segunda linha é {maior}') 
