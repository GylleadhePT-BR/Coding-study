def leiaint(txt):
    while True:
        print('-' * 45)
        n = str(input(txt))
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}')
            break
        else:
            print('\033[0;0;31mERRO!! digite um valor válido..\033[m')



numero = leiaint('Digite um numero : ')