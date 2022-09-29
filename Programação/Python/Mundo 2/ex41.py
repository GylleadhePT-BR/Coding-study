from datetime import date
atual = date.today().year
nome = input('Qual o seu nome : ')
nascimento = int(input('Qual o ano de nascimento  : '))
idade = atual-nascimento
if idade <= 9 :
    print('{} tem {} anos e è uma atleta de classificação MIRIM'.format(nome,idade))
elif idade > 9 and idade <= 14 :
    print('{} tem {} anos e é um atleta de classificação INFANTIL '.format(nome,idade))
elif idade > 14 and idade <= 19 :
    print('{} tem {} anos e é uma atleta de classificação JUNIOR'.format(nome,idade))
elif idade >19 and idade <=25 :
    print('{} tem {} anos e é um atleta de classificação SÊNIOR'.format(nome,idade))
elif idade >25:
    print('{} tem {} anos e é um atleta de classificação MASTER'.format(nome , idade))