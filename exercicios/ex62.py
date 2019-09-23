"""
EXERCÍCIO 062: Super Progressão Aritmética v3.0
Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
t = int(input('Primeiro termo: ')) 
r = int(input('Razão: ')) 
c = 0
n = 10
while c < n:
    print('{} > '.format(t),end=' ')
    t += r
    c += 1
    if n == c:
        print('PAUSA') 
        n += int(input('Quantos termos você quer mostrar a mais? ')) 
    
print('A progressão foi finalizada com {} termos mostrados'.format(c))

