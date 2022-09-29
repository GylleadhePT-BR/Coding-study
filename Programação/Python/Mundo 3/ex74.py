from random import randint
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('Os numeros sorteados foram : ',end='')
for numero in n:
    print(f'{numero} ',end='')
print(f'\nO maior valor sorteado foi {max(n)} e o menor foi {min(n)}')



