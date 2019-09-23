"""
Exercício Python 096: Faça um programa que tenha 
uma função chamada área(), que receba as 
dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.
"""

def area(larg, comp):
    print(f'A área do terreno é {larg*comp}m²') 
    
    
larg = int(input('Digite a largura do terreno: ')) 
comp = int(input('Digite o comprimento do terreno: ')) 
area(larg, comp) 
