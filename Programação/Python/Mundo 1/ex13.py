salario = float(input("Qual o salario :"))
aumento = int(input('Qual aumento foi aplicado:'))
cauculo = (100+aumento)/100
c2 = cauculo*salario
print('O funcionário que recebia um salario de R${:.2} , agora com um aumento de {}% vai receber R${:.2}'.format(salario,aumento,c2))
