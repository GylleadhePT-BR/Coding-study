from datetime import datetime
anoatual = datetime.today().strftime('%Y')
resp = 'sim'
print('-=-'*40)
print('BEM VINDO AO ALISTAMENTO MILITAR')
print('-=-'*40)
while resp == 'sim':
            nome = input('Digite seu nome :')
            ano_nasc = int(input('Digite o ano em que você nasceu :'))
            idade = int(anoatual) - int(ano_nasc)
            if idade < 18:
                print(
                    f"Olá {nome} , infelizmente você ainda não tem 18 anso , faltam {18 - idade} anos")
            if idade > 18 and idade < 50:
                print(
                    f"Olá {nome} , Se passaram {idade - 18} anos ,VOCÊ PRECISA SE ALISTAR!!!")
            if idade > 50:
                print(
                    f"Olá {nome} , você tem {idade} anos de idade e não será mais necessario se alistar..")
            resp = input('Deseja continuar : [sim/nao] ')
            if resp == 'nao':
                print('Finalizando o programa...')

