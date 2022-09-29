# coding=utf8
from time import sleep
numero = int(input('Digite um numero inteiro : '))
print ('escolha uma base de conversão: ')
print('''[1] converter para BINÀRIO 
[2] converter para OCTAL 
[3] converter para HEXADECIMAL ''')
opcao = int(input('Sua opção : '))
if opcao == 1:
    print('O seu valor em BINÀRIO é {}'.format(bin(numero)[2:]))
elif opcao == 2:
    print('O seu valor em OCTAL é {}'.format(oct(numero)[2:]))
elif opcao == 3 :
    print('O seu valor em HESADECIMAIS é {}'.format(hex(numero)[2:]))
else:
    print('OPÇÂO INVÀLIDA< POR FAVOR TENTE NOVAMENTE....')

