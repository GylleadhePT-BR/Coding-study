sex = str(input('por favor informe seu sexo [M/F]: ')).strip().upper()[0]
while sex not in "MmFf":
    sex = str(input('Sexo inválido....Digite novamente : ')).strip().upper()[0]
print('Sexo registrado com sucesso !!')
