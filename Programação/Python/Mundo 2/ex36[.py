# conding = utf8
casa = float(input('Qual o pre�o da casa :'))
salario = float(input('Qual o seu salrario : R$'))
anos = int(input('Em quantos anos deseja pagar : '))
prestacao = casa/(anos*12)
minimo = salario*30/100
print('Para pagar uma casa de R${} , a presta��o ser� de R${}.'.format(casa , prestacao))
if prestacao <= minimo :
    print('Empr�stimo aprovado.')
else:
    print('Empr�stimo negado.')
