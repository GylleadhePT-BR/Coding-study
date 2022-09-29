import random
from time import  sleep
from random import randint
print('{:=^40}'.format(' PEDRA PAPEL E TESOURA '))
sleep(1)
print('''Suas opções 
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual a sua jogada : '))
itens = ('PEDRA','PAPEL','TESOURA')
pc = random.randint(0,2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POW!!')
print('-=-'*10)
print('O jogador escolheu {}'.format(itens[jogador]))
print('O computador escolheu {}'.format(itens[pc]))
print('-=-'*10)
# jogadas do computador
if pc == 0 :
    if jogador == 0 :
        print('EMPATE')
    elif jogador == 1 :
       print('O JOGADOR VENCEU!!')
    elif jogador == 2 :
        print('O COMPUTADOR VENCEU!!')
    else:
        print('JOGADA INVÀLIDA!!')
elif pc == 1 :
    if jogador == 0 :
       print('O COMPUTADOR VENCEU!!')
    elif jogador == 1 :
       print('EMPATE')
    elif jogador == 2 :
        print('O JOGADOR VENCEU!!')
    else:
        print('JOGADA INVÀLIDA!!')
elif pc == 2 :
    if jogador == 0 :
        print('O JOGADOR VENCEU!!')
    elif jogador == 1 :
        print('O COMPUTADOR VENCEU!!')
    elif jogador == 2:
        print('EMPATE!!')
    else:
        print('JOGADA INVÀLIDA')

