from time import sleep

def numero_maior(*num):
    print('-='*20) 
    print('Analizando valores...')
    
    for x in num:
        print(x,end=' ', flush=True) 
        sleep(0.2)
    print(f'Foram informados {len(num)} valores.') 
    print(f'O maior valor informado foi {max(num)}') 
        

numero_maior(1,2,3,4)
numero_maior(8,7,9,8,7,6)
numero_maior(8,0,5,4,7)
numero_maior(1,2,3,1,2,0,9,8,11,8)