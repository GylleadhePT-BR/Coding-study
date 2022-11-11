class Cliente():
    def __init__(self , nome , idade):
        self.nome = nome
        self.idade = nome
        self.endereços = []
        
    def Insere_endereco(self , cidade , estado):
        self.endereços.append(Endereco(cidade, estado))
        
    def listar(self):
        for endereco in self.endereços:
            print(f'{self.nome} mora na cidade de {endereco.cidade} no estado de {endereco.estado}')
        
        
        
        
class Endereco():
    def __init__(self , cidade  , estado):
        self.cidade = cidade
        self.estado = estado