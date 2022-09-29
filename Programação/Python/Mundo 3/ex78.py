num = []
for c in range (0,5):
    num.append(int(input('Digite um valor : ')))
    maior = max(num)
    menor = min(num)
print(f'A lista {num} \nTem {len(num)} numeros sendo o menor deles {menor} e o maior {maior} ')
print(f'onde o numero {menor} está na posição {pos2} e o numero {maior} está na posição {pos1}')
