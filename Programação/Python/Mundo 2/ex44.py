print('{:=^40}'.format("LOJAS GUANABARA"))
preço = float(input('Preço das comprar : R$ '))
print('''Formas de pagamento :
[1] à vista dinheiro\cheque
[2] à vista cartão crédito
[3] 2x no cartão
[4] 3x ou mais no cartão''')
pagar = int(input('Como deseja pagar : '))
if pagar == 1 :
    total = preço - ( preço * 10 / 100)
    print('Pagando a vista com 10% de desconto você irá pagar R${}'.format(total))
elif pagar == 2 :
    total = preço - (preço * 5 / 100 )
    print('Pagando a vista pelo cartão de crédito , com desconto de 5% você irá pagar R${}'.format(total))
elif pagar == 3 :
    total = preço
    parcela = preço / 2
    print('Pagando 2x vezes sem juros parcelados no cartão o produto irá custar R${:.2f}'.format(parcela))
elif pagar == 4 :
    total = preço + (preço * 20 / 100)
    totparc= int(input('Quantas parcelas : '))
    parcela = total / totparc
    print('Sua conta será parcela {}x com juros e irá custar R${:.2f}'.format(totparc , parcela))
print('Sua compra de R${} irá custar R${}'.format(preço , total))

