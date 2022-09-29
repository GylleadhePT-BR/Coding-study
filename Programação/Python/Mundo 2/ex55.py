maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso registrado foi {}Kg'.format(maior))
print('E o menor peso registrado foi {}kg'.format(menor))