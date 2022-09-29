n = []
resp = 'S'
while resp == 'S':
    num = (int(input('Digite um valor : ')))
    if num not in n:
        n.append(num)
        print('Valor adicionado com sucesso.....')
    else:
        print('Valor duplicado , não adicionado...')
    resp = str(input('Deseja continuar ? [N/S] ')).strip().upper()
if resp == 'N':
    n.sort()
    print('-'*30)
    print(f'Você digitou os valores {n}')