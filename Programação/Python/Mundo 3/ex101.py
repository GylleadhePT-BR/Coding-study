#coding UTF-8
from datetime import date
def voto (nasc):
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        print(f'Você tem {idade} anos , Ainda não pode votar..')
    elif idade >= 18 :
        print(f'Você tem {idade} anos , o voto é obrigátório...')
    elif idade >= 65 :
        print(f'Você tem {idade} , o voto é opicional...')


voto(nasc = int(input('Em qua ano você nasceu :')))