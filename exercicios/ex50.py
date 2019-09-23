t = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for x in range(1,11):
    print(t, ' > ' , end=' ')
    t += r
print('ACABOU') 