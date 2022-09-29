hom = maior = mulher = 0
while True :
    idade = int(input('Idade : '))
    sexo = ' '
    while sexo not in "FfMm":
        sexo = str(input('Sexo [M/F] : ')).strip().upper()[0]
    if sexo in "F" and idade < 20:
        mulher += 1
    if sexo in "M":
        hom += 1
    if idade >= 18 :
        maior += 1
    escolha = ' '
    while escolha not in "SsNn":
            escolha = str(input('Deseja continuar [S/N] : ')).strip().upper()
    if escolha == "N":
        break
print(f'Analisamos {maior} pessoa maiores de 18..')
print(f'{hom} homens cadastrados..'if hom > 1 else f'{hom} homem cadastrado')
print(f'e {mulher} mulheres com menos de 20 anos..')