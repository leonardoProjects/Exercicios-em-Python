"""
EXERCÍCIO 043: Índice de Massa Corporal
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input('Digite seu peso: ')) 
altura = float(input('Digite sua altura: ')) 

imc = peso / (altura**2)

print('Seu imc é {:.2f}'.format(imc)) 

if 25 >= imc >= 18.5:
    print('Peso ideal!')
elif 30 >= imc >= 25:
    print('Sobrepeso!')
elif 40 >= imc >= 30:
    print('Obesidade!')
elif imc > 40:
    print('Obesidade mórbida!')
