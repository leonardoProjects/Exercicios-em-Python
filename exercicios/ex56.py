"""
EXERCÍCIO 056: Analisador Completo
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
nIdade = 0
idadeMaior = 0
menor = 0
nomePessoa = None
for i in range(1,5):
    print('- - - - - - {}° Pessoa - - - - - - '.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: ')) 
    sexo = input('Sexo [M/F]: ').strip().upper()
    nIdade += idade
    if idade > idadeMaior:
        if sexo == 'M':
            idadeMaior = idade
            nomePessoa = nome            
    if idade < 20 and sexo == 'F':
        menor += 1
        
media = nIdade / 4
print('~='*21) 
print('A média das idades é: {}'.format(media)) 
if nomePessoa != None:
    print('O homem mais velho é {} com {} anos.'.format(nomePessoa,idadeMaior))
print('{} mulheres tem menos de 20 anos'.format(menor))
print('~='*21) 