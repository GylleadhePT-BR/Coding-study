frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso  = ''
for  letra in range (len(junto)-1,-1,-1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == frase :
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')
