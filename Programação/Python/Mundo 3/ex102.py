from math import factorial


def fatorial(numero):
    resp = str(input('Deseja mostrar o cauculo ? [S/N]  :')).strip().upper()
    if resp in "Ss":
        print(f'O cauculo fatorial do numero informado é :')
        print(f'{numero}! = ',end='')
        for c in range(numero,0,-1):
            print(f'{c} * ',end='')
        print('= ',end='')
        print(factorial(numero))
    if resp in "Nn":
        print(f'O fatorial do numero informado é : ')
        print(f'{numero}! = {factorial(numero)}')


fatorial(numero = int(input('Digite um valor para adiquirir seu fatorial :')))
