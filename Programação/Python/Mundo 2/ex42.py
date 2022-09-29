print('-=-'*30)
print('Analisador de Triângulos..')
print('-=-'*30)
a = float(input('Digite o primeiro segmento : '))
b = float(input('Digite o segundo segmento : '))
c = float(input('Digite o terceiro segmento : '))
if a<b+c and b<a+c and c<a+b:
    print('Os segmentos podem formar um triângulo ',end='')
    if a==b==c :

     print('EQUILÀTERO')

    elif a!=b!=c!=a:

        print('ESCALENO')

    else:
        print('ISOCELES')
else:

    print('Os segmentos nâo formam um triângulo')

