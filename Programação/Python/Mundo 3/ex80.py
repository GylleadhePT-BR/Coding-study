valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}º valor: ')))
ordem = str(sorted(valores)).replace('[', '').replace(']', '')
print('-' * 30)
print(f'Ordem crescente: {ordem}')
