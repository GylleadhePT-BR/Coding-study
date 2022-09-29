somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho =''
totmulher20 = 0
for c in range ( 1, 5):
    print('----------------- {}ª PESSOA ----------------'.format(c))
    nome = input('Nome : ').strip()
    idade = int(input('Idade : '))
    sex = input('Sexo[M\F] : ').strip()
    somaidade += idade
    if c == 1 and sex in "Mm":
        maioridadehomem = idade
        homemmaisvelho = nome
    if sex in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        homemmaisvelho = nome
    if sex  in "Ff" and idade < 20 :
        totmulher20 += 1
mediaidade = somaidade/4
print('A média de todas as idade é {} '.format(mediaidade))
print('O  homem mais velho tem {} anos e se chama {} '.format(maioridadehomem,homemmaisvelho))
print('Ao todo são {} mulhers com menos de 20 anos'.format(totmulher20))
