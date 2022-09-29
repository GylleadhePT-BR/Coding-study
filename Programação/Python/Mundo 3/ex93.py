jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador(a) : '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou : '))
if jogador['partidas'] != 0:
    for g in range(0,jogador['partidas']):
        gols.append(int(input(f'    Quantos gols na partida {g+1} : ')))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
print('=-'*40)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]}. ')
for k , i in enumerate(jogador['gols']):
    print(f' ==> Na partida {k+1} , fez {i} gols')
print(f'Num total de {jogador["total"]} gols')

