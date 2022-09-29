from random import randint
v = 0
while True:
    Jogador = int(input('Digite um valor : '))
    computador = randint(0,10)
    total = Jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input('Par ou Impar [P/I] : ')).strip().upper()
        print(f'Você jogou {Jogador} e o computador {computador} total de {total}',end='')
        print(" Deu par" if total % 2 == 0 else " Deu Impar")
        if tipo == 'P':
            if total % 2 == 0 :
                print('Você venceu !!')
                v += 1
                print('vamos jogar novamente...')
            else:
                print('Você perdeu!!')
                print(f"GAME OVER!!, voce acertou {v} vezes")
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você Venceu!!')
                v += 1
                print('vamos jogar novamente...')
            else:
                print('Você perdeu')
                print(f"GAME OVER!!, voce acertou {v} vezes")
                break

