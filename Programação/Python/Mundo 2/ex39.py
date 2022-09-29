
from time import sleep
from datetime import date
atual = date.today().year
print('\033[0;31;0m-=-'*20)
print('ALISTAMENTO MILITAR..')
print('\033[0;31;0m-=-'*20)
sleep(2)
nome = input('Qual o seu nome : ')
if nome == 'gylleadhe':

    idade = int(input('Que nome bonito , seja bem vindo gylleadhe, nos informe sua idade:'))
else:
    idade = int(input('Seja bem vindo {} , nos informe sua idade :'.format(nome)))

if idade > 18 :
    saldo = idade - 18

    print('Okay {}, está tudo certo e você já tem a idade esperada deveria ter se alisatado a {} anos , pode pegar o seu comprovante'.format(nome,saldo))
elif idade == 18 :
        print('Você tem 18 anos deve se alistar agora!')

else:
    saldo = 18 - idade
    print('okay {} você ainda não tem a idade permitida que é 18, seu alistamento será daqui a {} anos'.format(nome,saldo))
print('-=-'*20)
