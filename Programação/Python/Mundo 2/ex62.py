print('Progressão aritmética')
print('-=-'*20)
p1 = int(input('Digite o primero termo : '))
r = int(input('E a razão : '))
termo = p1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} '.format(termo),end='')
        termo += r
        cont += 1
    print('Aguardando....')
    mais = int(input('Quantos termos você quer a mais : '))
print('A progressão foi finalizada com {} termos.'.format(total))