"""
EXERCÍCIO 083: Validando Expressões Matemáticas
Crie um programa onde o usuário digite uma
expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com
os parênteses abertos e fechados na ordem correta.
"""

expre = input('Digite um expressão: ')
pilha = []

for p in expre:
    if p == '(':
        pilha.append('(')
    elif p == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

print(pilha) 
if len(pilha) == 0:
    print('Expressões está válida!')
else:
    print('Expressão está errada!')
