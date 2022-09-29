dias = int(input('Quantos dias alugados : '))
km = float(input('Quantos kilometros rodados :'))
cauculo = (dias * 60) + (km * 0.15)
print('O total a pagar é R${}'.format(cauculo))
