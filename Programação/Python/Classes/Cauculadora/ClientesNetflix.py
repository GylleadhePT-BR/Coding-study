class Cliente():
    def __init__(self, nome,  email, plano ,):
        self.nome = nome
        self.email = email
        planos = ['basic' , 'premium' , 'medium']
        if plano in planos:
            self.plano = plano
        else:
            print("PLANO INVÀLIDO")


name = Cliente.nome(input('digite seu nome : '))
Email = Cliente.email(input('Digite seu email : '))
Plano = Cliente.plano(input('Digite o sue plano : '))

cliente1 = Cliente(name , Email , Plano)
print(Cliente.nome , Cliente.plano  , Cliente.email)
