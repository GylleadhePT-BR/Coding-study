soma = 0
total = 0
while True:
    num = int(input('digite um valor : '))
    if num == 99:
        break
    total = total + 1
    soma = soma + num
print(f'você infromou {total} numeros , A soma dos numeros foi {soma} ')
