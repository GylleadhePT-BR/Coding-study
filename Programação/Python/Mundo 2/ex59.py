from time import sleep
p1 = int(input('Digite o primero valor : '))
p2 = int(input('Digite o segundo valor : '))

opção = 0
while opção != 5:
    sleep(0.5)
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] sair''')
    opção = int(input('>>>>>>>> Informe sua opção : '))
    print('-=-'*20)
    if opção ==  1  :
        print('A soma entre {} e {} é {}'.format(p1,p2,p1+p2))
    elif opção == 2:
        print(' A multiplicação de {} e {} é igual a {}'.format(p1,p2,p1*p2))
    if opção == 3:
        if p1 > p2:
            maior = p1
            print('Entre {} e {} o maior é {}'.format(p1,p2,maior))
        elif p2 > p1 :
            maior = p2
            print('Entre {} e {} o maior é {}'.format(p1,p2,maior))
    if opção == 4 :
        print('Digite novos numeros....')
        p1 = int(input('Digite um valor : '))
        p2 = int(input('Digite mais um valor :'))
    elif opção == 5:
        print('Finalizando programação....')
    elif opção != 5 or 4 or 3 or 2 or 1:
        print('Opção inválida , tente novamente...')
    print('-=-' * 20)
print('Obrigado...')

