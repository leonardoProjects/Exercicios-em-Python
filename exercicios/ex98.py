"""
Exercício Python 098: Faça um programa que
tenha uma função chamada contador(), que 
receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens
através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep

def contagem(inicio, fim, passo=1):
    print('-=' *20)
    print(f'Contando de {inicio} a {fim} com passo {passo}') 
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
        
    if inicio < fim:
        fim += 1        
    elif inicio > fim:
         passo = passo * -1
         fim -= 1
        
    for x in range(inicio,fim,passo):
        print(x, end=' ', flush=True)  
        sleep(0.5) 
    print() 
        
contagem(1,10,1) 
contagem(1,10,2)
print('-='*20)

inicio = int(input('Início: ')) 
fim = int(input('Fim: ')) 
passo = int(input('Passo: ')) 

contagem(inicio, fim, passo) 








