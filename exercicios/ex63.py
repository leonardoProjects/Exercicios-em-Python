"""for x in range(1,11):
    for c in range(1,11):
        print('{} × {} = {}'.format(c, x,x*c))
    print('')
"""

num = input('Digite um número: ')

if len(num) >= 5:
    print(num[:5]) 