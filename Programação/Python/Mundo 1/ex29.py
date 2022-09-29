vel = float(input('Qual a velocidade do carro : '))
cauculo =(vel-80)*7
if vel>80 :
    print('-='*20)
    print('VOCÊ EXEDEU O LIMITE DE VELOCIDADE!!!! O VALOR DA MULTA SERA R${:.2f}'.format(cauculo))
    print('-='*20)
else:
    print('Sua velocidade está dentro dos limites , prossiga com sua rota.')
