# coding=utf8
nome = str(input('Olá qual o seu nome ?'))
v = nome.split()
print('O seu primeiro nome é {}'.format(v[0]))
print(' O seu ultimo nome é {}'.format(v[len(v)]-1))



