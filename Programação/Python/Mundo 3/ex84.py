nomepeso = []
rever = []
maior = menor = 0
while True:
    nomepeso.append(str(input('Nome : ')))
    nomepeso.append(float(input('Peso : ')))
    if len(rever) == 0:
        maior = menor = nomepeso[1]
    else:
        if nomepeso[1] > maior:
            maior =  nomepeso[1]
        if nomepeso[1] < menor:
            menor = nomepeso[1]
    rever.append(nomepeso[:])
    nomepeso.clear()
    resp = str(input('Deseja continuar ? [N/S] ')).strip().upper()[0]
    if resp == 'N':
        print('-'*50)
        print(f'Ao todo foram cadastradas {len(rever)} pessoas ')
        print(f'O maior peso registrado foi {maior}Kg De : ')
        for p in rever:
            if p[1] == maior:
                print(f'{p[0]}')
        print(f'O menor peso registrado foi {menor}Kg De : ')
        for p in rever:
            if p[1] == menor:
                print(f'{p[0]}')
        print('Fim do programa..')
        break
