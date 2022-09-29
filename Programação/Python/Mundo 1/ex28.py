import random
from time import sleep
nome = input("\u001b[31mQual o seu nome ?")
print('\033[0;0;31m =-\033[m'*20)
print('\033[0;0;35mOkay {} , eu irei pensar num numero entre 0 e 10 tente advinhar...'.format(nome))
c = random.randint(0,10)
print('\033[0;0;31m =-\033[m'*20)
numero = input("Qual numero eu pensei ?")
print('PROCESSANDO...')
sleep(2)
if numero==c:
    print('Parabens!! , você acertou , o numero que eu pensei foi {}'.format(c))
else:
    print('Você errou!! , o numero que eu pensei foi {}'.format(c))
print('\033[0;0;31m =-\033[m'*20)