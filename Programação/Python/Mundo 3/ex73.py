times = ('Esporte','Nautico','Atlético','Fluminense','Vasco','Curitiba','chapecoense','são paulo','ssanta','cruzeiro')
print('-'*40)
print(f'Lista dos times Brasileiros : {times}')
print('-'*40)
print(f'Os primeiros 5 times são : {times[:5]}')
print('-'*40)
print(f'Os quatro ultimos são {times[-4:]}')
print('-'*40)
print(f'Times em ordem Alfabética : {sorted(times)}')
print('-'*40)
print(f'Chapecoense está na {times.index("chapecoense")}ª posição')
print('-'*40)