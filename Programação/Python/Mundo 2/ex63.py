print('{:-^60}'.format('Sequência de Fibonacci'))
termos = int(input('QUantos termos você quer mostrar : '))
t1 = 0
t2 = 1
print('~'*60)
print(' {} {} '.format(t1,t2),end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print('{} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\nPrograma finalizado.....')
