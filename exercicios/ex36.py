"""
DESAFIO 036: Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anos = int(input('Quantos anos irá pagar: '))
minimo = (salario * 30) / 100
parcelas = casa / (anos * 12)

if parcelas <= minimo:
    print('Empréstimo concedido!') 
    print('Em {} anos você irá pagar R${:.2f} por mês'.format(anos, parcelas)) 
else:
    print('Empréstimo negado!!') 




