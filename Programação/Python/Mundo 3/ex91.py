from time import sleep
from random import randint
from operator import itemgetter
jogadores = {'jogador 1':randint(1,6),
            'jogador 2' :randint(1,6),
             'jogador 3':randint(1,6),
             'jogador 4': randint(1,6)}
print('-'*20)
print('VALORES SORTEADOS')
print('-'*20)
ranking = list()
for k,v in jogadores.items():
    sleep(1)
    print(f'O {k} tirou {v}')
ranking = sorted(jogadores.items() , key=itemgetter(1),reverse=True)
print('-'*20)
print('RANKING')
print('-'*20)
for i , v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º Lugar : {v[0]} dado : {v[1]}')
print('Obrigado volte sempre...')
