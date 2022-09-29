
nome = input('Digite seu nome : ')
while len(nome) < 3:
    nome = input('ERRO!! , digite um nome valido : ')
    if len(nome) > 3:
        print('NOME CADASTRADO')



idade = int(input('Digite sua idade : '))
while idade <= 0  or idade >= 150:
    idade = int(input(' ERRO !! Digite sua idade : '))
    if (idade <= 0  or idade >= 150) == True:
        print('IDADE ACEITA')


salario = float(input('Digite o seu salario R$ : '))
while salario < 0:
    salario = float(input(' ERRO!! Digite o seu salario R$ : '))
    if salario > 0:
        print('SALARIO CADASTRADO!!') 

    
sexo = input('Digite seu sexo [M/F] : ').upper()
while sexo != 'M' and sexo !='F':
    sexo = input('ERRO!! Digite seu sexo [M/F] : ')
    if sexo == 'M' and sexo =='F':
        print('PESSOA CADASTRADA')
    

estado_civil = input('Digite seu estado estado civil : ')

while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'd' and estado_civil != 'v':
    estado_civil = input(' ERRO !! Digite seu estado estado civil : ')
    if estado_civil == 's' and estado_civil == 'c' and estado_civil == 'd' and estado_civil == 'v':
        print('ESTADO CIVIL CADASTRADO')
        print('OBRIGADO por ultilizar nosso programa...')
        break






