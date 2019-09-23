import random
acertou = 0
while True:
    num = int(input('Digite um número: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Ímpar ou par [I/P]: ').upper().strip()[0]
    num_gerado = random.randint(1,9)    
    print(f'Você jogou {num} e o computador jogou {num_gerado}') 
    print(f'Total de {num + num_gerado}')   
    if (num + num_gerado) % 2 == 0:
        print('Deu par') 
        if escolha in 'Pp':
            print('Você ganhou!') 
            acertou += 1
        else:
            print('Você perdeu!') 
            break
    else:
        print('Deu ímpar') 
        if escolha in 'iI':
            print('Você ganhou!') 
            acertou += 1
        else:
            print('Você perdeu!') 
            break            
print(f'Total de vitórias {acertou}') 