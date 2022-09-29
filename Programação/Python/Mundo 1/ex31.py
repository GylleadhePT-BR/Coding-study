distancia = float(input('Qual a distância da viagem : '))
desconto = distancia*0.45
preço =distancia*0.50
if distancia<=200:
    print('Numa viagem de {:.2f}Km a preço será R${:.2f}'.format(distancia,preço))
else:
    print('Numa viagem de {:.2f}Km o preço a pagar será R${:.2f}'.format(distancia,desconto))