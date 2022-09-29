print('{:=^40}'.format('Tabuada 3.0'))
while True:
    num = int(input('Qual numero deseja analisar [Digite 0 para finalizar o programa] : '))
    if num<0:
        print('Valor inválido....')
        break
    elif num == 0:
        print('Obrigado por usar o programa , finalizando codigo....')
        break
    print('-=-'*30)
    for c in range (1,11):
        print(f'{num} x {c} = {num*c}')
    print('-=-'*30)

