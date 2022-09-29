import random
a = input('Qual o primero aluno ?')
b = input('Qual o segundo aluno ?')
c = input('Qual o terceiro aluno ?')
d = input('Qual o quarto aluno ?')
lista = [a,b,c,d]
random.shuffle(lista)
print('A ordem aprasentada será , {}'.format(lista))
