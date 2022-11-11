
class Produto:
    def __init__(self, Nome, preco, quantidade):
        self.nome = Nome
        self.preco = preco
        self.quantidade = quantidade
        
        
    #Getter
    @property
    def poreco(self):
        return self._preco
    
    #setter
    @preco.setter
    def preco(self, valor):
        if isinstance( valor , str):
            valor  = float(valor.replace('R$' , ''))
            
        self._preco = valor
        
    def atualizarPreco(self):
        print('Voce solicitou uma atualização de preco.')
        self.preco = float(input('Digite o novo preço : '))

    def desconto(self):
        percentual = int(input('Digite a porcentagem do seu desconto : '))
        self.preco = self.preco - (self.preco * (percentual / 100))
        print(f'Seu proudto com {percentual}% de desconto está custando R${self.preco}..')

    def aumentarQuantidade(self):
        print('A quantidade atual do sue pedido é', self.quantidade)
        self.quantidade = input('Quantas unidades deseja adicionar : ')
        print('Tudo certo..agora tens ',
              self.quantidade, 'unidades desse produto')


cliente1 = Produto(input('Digite o nome do produto : '), float(input('Digite o preco do produto : ')),int(input('Digite A quantidade de unidades do sue pedido : ')))
print(cliente1.desconto())
