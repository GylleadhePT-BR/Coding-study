print('='* 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar : R$ '))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total-=cedula
        totalcedula += 1
    else:
        print(f'Total de {totalcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
print('='*30)
print('Obrigado Volte sempre!!')
