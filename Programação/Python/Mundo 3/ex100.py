def numeros(*num):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares na lista numerica {num} é igual a {soma}')


