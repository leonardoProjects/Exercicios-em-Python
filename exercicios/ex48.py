"""
EXERCÍCIO 049: Tabuada v2.0
Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
num = int(input('Digite um número para ver sua tabuada: '))
for i in range(1,11):
    print('{} × {} = {}'.format(num, i , num * i))
print('Fim')
