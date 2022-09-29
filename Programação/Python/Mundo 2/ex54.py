maioridade = 0
menor = 0
from datetime import date
atual = date.today().year
for p in range (1,8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa : '.format(p)))
    idade = atual - nasc
    if idade >= 18 :
        maioridade += 1
    else:
        menor += 1
print('Ao todo tivemos {} pesosa de maioridade e {} de menoridade'.format(maioridade,menor))


