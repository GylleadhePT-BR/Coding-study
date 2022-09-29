numeros = [[],[]]
valor = 0
for c in range (0,5):
    valor = int(input('Digite um valor : '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 == 1 :
        numeros[1].append(valor)
print('=-'*50)
numeros[0].sort()
numeros[1].sort()
print(f'A lista de todos os pares é : {numeros[0]}')
print(f'A lista de todos os impares é : {numeros[1]}')
