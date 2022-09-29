
nome = input('Qual o seu nome : ')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em menúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
c = nome.split()
print(' Seu primeiro nome é {}'.format(c[0]))

