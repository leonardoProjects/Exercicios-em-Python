"""
EXERCÍCIO 079: Valores Únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""
lista_de_numeros = [] 
cont = ' '
print('~='*20)
while cont not in 'N':
    numero = int(input('Digite um número: '))
    if numero not in lista_de_numeros:
        lista_de_numeros.append(numero)
        print('Número adicionado com sucesso!') 
        cont = input('Deseja continuar adicionando? [S/N] ').upper().strip()[0]
        print('~='*20)
    else:
        print(f'O numero {numero} já existe na lista.')
        
print('Números adicionados: ', end='')
lista_de_numeros.sort()
for n in lista_de_numeros:
    print(n, end=' ')
print() 



