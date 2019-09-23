"""
EXERCÍCIO 044: Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

preco = int(input('Digite o preço: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista no dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Escolha uma opção: ')) 

if opcao == 1:
    total = preco
    novo = preco - (preco * 10) / 100
elif opcao == 2:
    total = preco - (preco * 5) / 100
elif opcao == 3:
    parcelas = preco / 2
    total = preco
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS.'.format(parcelas))
elif opcao == 4:
    pac = int(input('Digite o número de parcelas: ')) 
    juros = (preco * 20) / 100
    parcela = preco / pac + juros
    total = preco + juros
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.'.format(pac, parcela))
else:
    print('Opção inválida!!') 
    print('Tente novamente!') 
    total = preco
    
print('O produto de R${} ira custar R${}'.format(preco, total))
