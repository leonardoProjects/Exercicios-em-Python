from random import randint
from time import sleep 

def gerar_num():
    lista = [randint(0,5) for x in range(0,5)]
    print('Números gerados:', end=' ') 
    for x in lista:
        print(x, end=' ', flush=True) 
        sleep(0.2)
    print() 
    return lista

def soma_par(numeros):
    print('A soma dos pares é:', end=' ') 
    soma = 0
    for x in numeros:
        if x % 2 == 0:
            soma += x
    print(soma) 
            
    
print('-='*20) 
numeros = gerar_num()
soma_par(numeros) 
print('-=' *20)