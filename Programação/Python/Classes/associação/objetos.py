class Escritor():
    def __init__(self , nome , idade):
        self.nome = nome
        self.idade = idade
        self.ferramenta = None


class Caneta():
    def __init__(self , cor , marca):
        self.marca = marca
        self.cor = cor 
        
    def escrever(self):
        print('Caneta esta escrevendo.....')
    
class MaquinaEscrever():
    def __init__(self , nome):
        self.nome = nome
    
    def escrever(self):
        print('A maquina esta escrevendo...')
        