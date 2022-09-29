numero1 = int(input('Digite o primeiro valor : '))
numero2 = int(input('Digite o segundo valor : '))
numero3 = int(input('Digite o terceiro valor :'))
#menor
menor = numero1
if numero2<numero1 and numero2<numero3:
     menor = numero2
if numero3<numero1 and numero3<numero2:
         menor = numero3
#maior
maior = numero1
if numero2>numero1 and numero2>numero3:
    maior = numero2
if numero3>numero1 and numero3>numero2:
        maior = numero3
print('O maior valor digitado é {}'.format(maior))
print('O menor valor digitado é {}'.format(menor))



