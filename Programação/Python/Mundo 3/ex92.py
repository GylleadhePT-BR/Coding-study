from datetime import date
atual = date.today().year
cidadao = {}
cidadao['nome'] = str(input('Nome : '))
cidadao['nasci'] = int(input('Ano de nascimento : '))
cidadao['ct'] = int(input('Carteira de trabalho (Digite 0 caso não possuir ) : '))
cidadao['idade'] = atual - cidadao['nasci']
if cidadao['ct'] == 0 :
    print('=-'*40)
    print(f'O cidadão {cidadao["nome"]} tem {cidadao["idade"]} e não tem carteira de trabalho..')
if cidadao['ct'] != 0 :
    cidadao['contratacao'] = int(input('Ano de contratação : '))
    cidadao['salario'] = float(input('Salario : '))
    cidadao['aposentadoria'] = cidadao['idade'] + ((cidadao['contratacao']+35) - atual)
    print(f'A pessoa :{cidadao["nome"]}'
          f'\nTem {cidadao["idade"]} anos'
          f'\nFoi contratada em {cidadao["contratacao"]}'
          f'\nE vai se aposentar com {cidadao["aposentadoria"]} anos de idade..')
print('Obrigado volte sempre..')
