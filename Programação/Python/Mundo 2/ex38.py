# coding=utf8
n1 = int(input('Digite um numero : '))
n2 = int(input('Digite mais um numero : '))
if n2 > n1 :
    print('O maior valor é {}'.format(n2))
elif n1>n2 :
    print('O maior valor é {}'.format(n1))
elif n1 == n2 :
    print('Não há valor maior ou menor , os dois são iguais.')
