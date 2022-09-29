numgerais = []
resp= 'S'
pares = []
impares =[]
while resp == 'S':
    num = int(input('Digite um numero : '))
    numgerais.append(num)
    resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if resp == 'N':
        print(f'A lista completa é : {numgerais.sort()}')
        for i, v in enumerate(numgerais):
            if v % 2 == 0:
                pares.append(v)
            elif v % 2 == 1:
                impares.append(v)
        print(f'A lista dos pares é {pares.sort()}')
        print(f'A lista dos impares é {impares.sort()}')

