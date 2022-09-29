from math import hypot
co = float(input(('Qual o comprimento do cateto oposto :')))
ca = float(input('Qual o comprimento do cateto adjascente :'))
print('O valor da hipotenusa dessas mediads é {:.2f}'.format(hypot(co,ca)))