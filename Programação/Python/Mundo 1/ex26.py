frase = str(input('Digite uma frase : ')).upper()
print('A letra "A" aparece {} vezes na sua frase.'.format(frase.count('A')))
print('A primeira letra "A" está na posição {} '.format(frase.find("A")+1))
print((' A ultima letra "A" apareceu na posição {}'.format(frase.rfind('A')+1)))
