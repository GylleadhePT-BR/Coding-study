pessoas = dict()
conjunto = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome : '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F] : ')).strip().upper()
        if pessoas['sexo'] in "MF":
            break
        print('ERRO!! , Digite apenas entre M e F..')
    pessoas['idade'] = int(input('Idade : '))
    soma += pessoas['idade']
    conjunto.append(pessoas.copy())
    while True:
        resp = str(input('Deseja continuar [S/N] : ')).strip().upper()[0]
        if resp in "SN":
            break
        print('ERRO!! , digite apenas S ou N..')
    if resp == 'N':
        break
print('=-'*60)
print(f'Ao todo temos {len(conjunto)} pessoas')
media = soma / len(conjunto)
print(f'A media da iade de todos é igual a {media}')
print(f'As mulheres cadastradas foram : ',end='')
for p in conjunto:
    if p['sexo'] in "Ff" :
        print(f'\n{p["nome"]}',end='')
print('=-'*40)
print(f'E os homens cadastradas foram :',end='')
for p in conjunto:
    if p['sexo'] in "Mm" :
        print(f'\n{p["nome"]}',end='')
print('\nObrigado..Volte sempre!!')
print('=-'*40)
