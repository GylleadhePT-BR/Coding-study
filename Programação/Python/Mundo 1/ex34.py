salario = float(input('Qual o seu salário : R$ '))
if salario<=1250 :
    aumento = salario+(15/100*salario)
    print('Você recebeu um aumento de 15% , seu salario de R${} , agora será R${}'.format(salario,aumento))
if salario>1250:
    aumento2 = salario+(10/100*salario)
    print('Você recebeu um aumento de 10% , seu salario de R${} , agora seá R${}'.format(salario,aumento2))

