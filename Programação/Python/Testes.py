numeros = []
for i in range(1,11):
    num = numeros.append(input(f'Digite o {i}º valor  : '))
    if num in list(numeros) :
        print('Esse numero ja foi digitado...')
print(f'O maior de todos os valores informado é {max(numeros , key=int)}')
