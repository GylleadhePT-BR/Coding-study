from random import choice
al1 = input("Qual o primeiro aluno :")
al2 = input('Qual o segundo aluno :')
al3 = input('Qual o terceiro aluno :')
al4 = input('Qual o quarto aluno : ')
lista =[al1,al2,al3,al4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
