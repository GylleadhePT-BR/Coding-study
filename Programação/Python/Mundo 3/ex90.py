dado = {}
dado['nome'] = str(input('Nome :'))
dado['media'] = float(input('Media : '))
if dado['media'] > 6 :
    print(f'Parabens você foi aprovado com media {dado["media"]}')
elif dado['media'] < 6 :
    print(f'Infelizmente a nota foi inferior a 6 você foi reprovado !')
elif dado['media'] == 6:
    print(f'Foi por ouco... você tirou 6 terá que fazer umaa prova de recuperação...')
print('Obrigado..volte sempre!')




















