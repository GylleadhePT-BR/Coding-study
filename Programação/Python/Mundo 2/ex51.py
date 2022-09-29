print('{:=^60}'.format(' PROGRESSÃO ARITMÉTICA '))
p1 = int(input('Qual o primeiro temro : '))
r = int(input('Informe a razão : '))
decimo = p1 + (10-1)*r
for pa in range (p1,decimo + r ,r):
    print('{} '.format(pa),end='')


