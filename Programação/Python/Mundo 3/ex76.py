produtos  = ('lápis',1.75,
             'borracha',2.00,
             'Lapiseira',2.50,
             'caderno',15.90,
             'Estojo',25,
             'mochila',120.50,
             'canetas',1.50,
             'livro',70.00)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(produtos)):
    if pos % 2== 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R${produtos[pos]:>10.2f}')