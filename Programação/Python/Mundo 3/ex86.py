matrix = []
for l in range(0,3):
    for c in range (0,3):
        matrix[l][c]= int(input(f'Digite um valor para [{l} , {c}] : '))
print('=-'*50)
for l in range(0,3):
    for c in range ( 0,3):
        print(f'[{matrix[l][c]:^5}]',end='')
    print()
