"""
EXERCÍCIO 094: Unindo Dicionários e Listas
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas cadastradas.
B) A média de idade.
C) Uma lista com mulheres.
D) Uma lista com idade acima da média.
"""
lista = []

while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: ')) 
    while True:
        sexo = str(input('Sexo [M/F] ')).upper().strip()[0]
        if sexo in 'MF':
            pessoa['sexo'] = sexo
            break
        else:
            print('Por favor digite apenas M ou F.') 
    pessoa['idade'] = int(input('idade: '))
    lista.append(pessoa)
    while True:
        cont = input('Quer continuar? [S/N] ').upper().strip()[0]
        if cont in 'SN':
            break 
        else:
            print('Por favor digite apenas Sim ou Não.')           
    if cont == 'N':
        break

print('-='*20)
print(f'Foram cadastradas {len(lista)} pessoas.')
tot_idade = 0
for pessoa in lista:
    tot_idade += pessoa['idade']
media_idade = tot_idade / len(lista) 
print(f'A media das idades foi {media_idade:.2f}')
print('As mulheres cadastradas foram: ', end='') 
for m in lista:
    if m['sexo'] == 'F':
        print(m['nome'], end=' ')
print() 
print('As idades acima da média foi de: ') 
for i in lista:
    if i['idade'] > media_idade:
        print(f' - {i["nome"]} com {i["idade"]}') 
print('-='*20)

 






