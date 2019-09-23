"""
EXERCÍCIO 065: Maior e Menor Valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

num = int(input('Digite um número [0 para parar]: ')) 
menor = num
maior = total = cont = 0
while num != 0:
    total += num
    cont += 1
    
    if menor > num:
        menor = num
        
    if maior < num:
        maior = num
        
    num = int(input('Digite um número [0 para parar]: ')) 
    
media = total / cont

print('\n') 
print(f'O maior número digitado foi {maior}') 
print(f'O menor número digitado foi {menor}') 
print(f'A média dos números é {media}') 