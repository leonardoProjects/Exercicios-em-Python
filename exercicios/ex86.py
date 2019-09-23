"""
EXERCÍCIO 086: Matriz em Python
Crie um programa que crie uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado.
0 [_][_][_]
1 [_][_][_]
2 [_][_][_]
   0  1  2
No final, mostre a matriz na tela, 
com a formatação correta.
"""
matriz = [[], [], []] 
for x in range(0,3):
    for i in range(0,3):
        num = input(f' a{x+1}{i+1}: ') 
        matriz[x].append(num) 
        
print('\nMatriz: ') 
for n in matriz:
    for z in n:
        print(f'[ {z} ]', end='  ')
    print() 