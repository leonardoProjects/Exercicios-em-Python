"""
EXERCÍCIO 082: Dividindo Valores em Várias Listas
Crie um programa que vai ler vários números e colocar
em uma lista. Depois disso, cria duas listas extras
que vão conter apenas os valores pares e os valores 
ímpares digitados, respectivamente. Ao final,
mostre o conteúdo das três listas geradas.
"""

list_number = []
list_number_im = []
list_number_pa = []

while True:
    number = int(input('Write a number: '))
    list_number.append(number)
    if number % 2 == 0:
        list_number_pa.append(number)
    else:
        list_number_im.append(number)
    cont = input('You want to continue? [Y/N] ').strip().upper()[0]
    if cont in 'N':
        break
    
print('~='*20)
print(f'The numbers are {list_number}')
print(f'The even numbers are {list_number_pa}')
print(f'The odd numbers are {list_number_im}')

