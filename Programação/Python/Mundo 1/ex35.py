print('-='*20)
print("Analisador de Triânguos")
print('-='*20)
a= float(input('Digite o primeiro segmento : '))
b = float(input('Digite o segundo segmento : '))
c = float(input('Digite o terceiro segmento : '))
if a<b+c and b<a+c and c<a+b:
    print('Os segmentos acima podem formar um triângulo .')
else:
    print('Os segmentos abaixo nao podem formar um triãgulo.')
