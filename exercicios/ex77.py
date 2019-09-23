"""
EXERCÍCIO 077: Contando Vogais em Tupla
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('Mercado','morango', 'banana', 
	           'Notebook', 'carro', 'celular') 

for palavra in palavras:
    palavra = palavra.upper()
    print(f'Na palavra {palavra} temos:',end='')
    for letra in palavra:
       if letra in 'AEIOU':
           print(letra, end='')
    print('\n')
       
       
           
           
        
        
