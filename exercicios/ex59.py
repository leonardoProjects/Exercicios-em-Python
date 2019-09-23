"""
EXERCÍCIO 059: Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
n1 = int(input('Digite um número: ')) 
n2 = int(input('Digite outro número: ')) 
sair = False
while not sair: 
    print('''
     [ 1 ] Somar
     [ 2 ] Multiplicar
     [ 3 ] Maior
     [ 4 ] Novos Números
     [ 5 ] Sair do Programa''') 
    opcao = int(input('Qual opção? ')) 
    if opcao == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1,n2,n1+n2)) 
    elif opcao == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('O número maior entre {} e {} é {}'.format(n1,n2,n1))
        else:
            print('O número maior entre {} e {} é {}'.format(n1,n2,n2))
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Fim do programa, volte sempre!')
        sair = True
    else:
        print('Opção inválida!!') 

       
