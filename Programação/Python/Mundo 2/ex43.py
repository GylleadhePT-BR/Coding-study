altura = float(input('Qual a sua altura : '))
peso = float(input('Qual o seu peso : '))
imc = peso / (altura**2)
print('O Seu IMC é de {:.2f}, '.format(imc),end='')
if imc < 18.5 :
    print('Você está ABAIXO do peso!')
elif imc >= 18.5 and imc <= 25 :
    print('Você está com PESO IDEAL!')
elif imc >= 25 and imc <= 30 :
    print('Você Está com SOBREPESO!')
else:
    print('Você está com OBESIDADE MORBIDA!')
