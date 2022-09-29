total = num = soma = 0
num = int(input('Digite os valores que deseja analisar , digite [99] para finalizar o programa :'))
while num != 99 :
    total = total + 1
    soma = soma + num
    num = int(input('Digite os valores que deseja analisar , digite [99] para finalizar o programa :'))
print('Você informou {} valores,e a soma entre eles foi {}'.format(total,soma))
