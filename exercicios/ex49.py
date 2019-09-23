"""
EXERCÍCIO 050: Soma dos Pares
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
s = 0
for x in range(1,7):
    num = int(input('Digite o {}° número: '.format(x)))
    if num % 2 == 0:
        s += num
print('A soma dos números pares é: {}'.format(s))