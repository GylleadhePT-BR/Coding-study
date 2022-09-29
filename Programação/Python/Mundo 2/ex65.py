resp = "S"
maior = menor = total = soma = media = 0
while resp in "S":
    num = int(input('Digite um numero :  '))
    soma  = soma + num
    total = total + 1
    if total == 1:
        maior = menor  =num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N] : ')).upper().strip()
media = soma/total
print('Voce digitou {} numeros e a média foi {}'.format(total , media))
print('Dos {} numereos que você informou {} é o maior e {} é o menor.'.format(total,maior,menor))



