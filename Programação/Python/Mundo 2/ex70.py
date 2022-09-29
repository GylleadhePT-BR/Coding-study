print('~~'*30)
print('LOJA SUPER BARATÂO')
print('~~'*30)
maisbarato  = total= totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto : '))
    preço = float(input('Preço do produto : '))
    resp = ' '
    total += preço
    if preço > 1000:
        totmil+=1
    if cont == 1:
        menor =  preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    while resp not in "SN":
        resp = str(input('Deseja continuar [S/N] :')).strip().upper()[0]
    if resp == 'N':
        break
print('{:=^40}'.format('FIM DO PROGRAMA'))
print(f'O total de compras foi R${total:.2f}')
print(f'{totmil} produto custou mais de Mil reais'if totmil == 1 else f'{totmil} produtos custaram mais que Mil reais')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}.')
