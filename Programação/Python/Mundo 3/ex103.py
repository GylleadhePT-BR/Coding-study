def jogador(nome , gols):
    if not nome:
        nome = '<Desconhecido>'
    if not gols or not gols.isnumeric():
        gols = 0
    print(f'O jogador {nome} fez {gols} gols ma partida..')




jogador(str(input('Nome do jogador: ')).strip(), str(input('Número de gols: ')).strip())


