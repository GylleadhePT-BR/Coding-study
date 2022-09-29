pares = 0
soma = 0
for num in range (1,7):
    v = int(input('Digite o {}º valor : '.format(num)))
    if v % 2 == 0:
        pares += 1
        soma = soma + v
print('A soma dos {} numeros pares é igual a {}'.format(pares,soma))
