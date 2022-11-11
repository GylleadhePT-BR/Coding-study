class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def falar(self):
        print('Deus é mais')


class CLiente(Pessoa):
    pass

class Aluno(Pessoa):
    pass