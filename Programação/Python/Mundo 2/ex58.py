from random import randint
computador = randint(0,10)
nome = str(input('Qual o seu nome : '))
len(nome)
if nome[-1] == "a":
    print('olá senhora {} , sou seu computador....'.format(nome))
else:
    print('OLá senhor {}  , sou seu computador....'.format(nome))
print('Acabei de pensar em um numero entre 0 e 10 tente advinhar...')
acertou = False
palpites = 0
while not acertou :
    jogador = int(input('Qual é o seu palpite : '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else :
        if jogador < computador :
            print('Mais...')
        if jogador > computador:
            print('Menos...')
print('Parabens voce acertou, o numero pensado foi {} !!'.format(computador))
print('Fim!!, depois de {} palpites'.format(palpites))
