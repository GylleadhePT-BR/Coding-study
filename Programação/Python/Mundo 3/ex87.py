matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapares = segundalinha =  somacoluna = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] :'))
print('=-'*50)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
    print()
print('=-'*50)
print(f'A soma dos numeros pares é {somapares}')
for l in range(0,3):
    somacoluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacoluna}')
for c in range (0,3):
    if c == 0:
        segundalinhas = matriz[1][c]
    elif matriz[1][c] > segundalinha:
        segundalinha = matriz[1][c]
print(f'O maior valor da segunda linha é {segundalinha}')
