choice = int(input('Enter to a number with your choice for do operation : [1] Soma
'[2] Subtração
'[3]  Divisão
'[4] multiplicão
'))
num = int(input('Digit your 1º number :'))
num2 = int(input('Digit your 2º number :'))
if choice == 1:
    print(f' {num} + {num2} is {num+num2} ')
if choice == 2:
    print(f'{num} - {num2} is {num-num2}')
if choice == 3:
    print(f'{num} / {num2} is {num/num2}')
if choice == 4:
    print(f'{num} * {num2} is {num *num2}')
print('Thanksfor using our program')
