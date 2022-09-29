from ex107modulo import moeda , dobro , metade , l , aumento

num = float(input('Digite um valor : '))
porcet = int(input('Quantos porcento você quer aumentar : '))
l('RESUMO DE VALOR !!')
print(f'Valor analisado:  \t{moeda(num)}')
print(f'A metade de {moeda(num)}:  \t{metade(num)}')
print(f'O dobro de {moeda(num)}:  \t{dobro(num)}')
print(f'{porcet}% de aumento de {moeda(num)}:  \t{moeda(aumento(num,porcet))}')
print('~'*20)