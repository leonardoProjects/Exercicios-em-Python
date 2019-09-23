"""
EXERCÍCIO 085: Listas com Pares e Ímpares
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista_num = [[], []] 
for x in range(1,8):
    num = int(input(f'Digite o {x}° número: '))
    if num % 2 == 0:
        lista_num[0].append(num)
    else:
        lista_num[1].append(num)
        
lista_num[0].sort()
lista_num[1].sort()
print('-='*20)
print('Os números pares são:', end=' ') 
for x in lista_num[0]:
    print(x,end=' ')
print() 

print('Os números ímpares são:', end=' ') 
for x in lista_num[1]:
    print(x,end=' ')
print() 
print('-='*20) 


    