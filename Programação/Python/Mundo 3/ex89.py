print('-'*40)
print('            BOLETIM ESCOLAR')
print('-'*40)
ficha = list()
while True:
    nome = str(input('Nome : '))
    n1 = float(input('Nota 1 : '))
    n2 = float(input('Nota 2 : '))
    media = (n1+n2)/2
    ficha.append([nome,[n1,n2],media])
    resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-'*40)
print(f'{"Nº":<4}{"NOTA":<10}{"MÈDIA":>8}')
print('-'*40)
for i , a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*40)
    opc = int(input('De qual aluno deseja mostrar as notas ? [99 para parar] :  '))
    if opc == 99:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são : {ficha[opc][1]}')
print('Volte sempre!')
