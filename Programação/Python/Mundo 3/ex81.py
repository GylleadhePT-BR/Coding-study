num = []
resp = 'S'
while resp == 'S':
    n = int(input('Digite um valor :  '))
    if n < 0:
        print('Não podemos analisar..')
        break
    else:
        num.append(n)
        resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()
if resp == "N":
    print('=-'*40)
    num.sort(reverse=True)
    print(f'Você digitou {len(num)} valores')
    print(f'Os valores em ordem decrescente são : {num}')
    if 5 in num:
        print('O valor cinco faz parte da lista')
    else:
        print('Não registramos nenhum 5')