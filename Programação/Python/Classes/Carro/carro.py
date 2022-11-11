class Carro():
    def __init__ (self , modelo,  Kmrodados , placa , valor_mercado_novo , condicao,  combustivel , kmlitros , obs ,valor_mercado_usado , defeito ,ligado = True ):
        self.modelo = modelo
        self.kmroados = Kmrodados
        self.placa = placa
        self.valor_mercado_novo = valor_mercado_novo
        self.condicao = condicao
        self.ligado = ligado
        self.combustivel = combustivel
        self.kmlitros = kmlitros
        self.obs = obs
        self.valor_mercado_usado = valor_mercado_usado
        self.defeito = defeito
        
        
        def ligar(self):
            if self.ligado == True:
                print('Seu carro ja esta ligado')
                esc = input('Deseja desligar ? [s/n] ')
                if esc == 's':
                    self.ligado = False
                    print('Seu carro foi desigado..')
                else:
                    print('Seu carro continua ligado')
        def abastecer(self):
            adicionar = input('Seu carro está com L',self.combustivel,'de combustivel..  deseja abastecer ? [s/n]')
            if adicionar == 's':
                litros = float(input('Quanto litros deseja abastecer ?'))
                cauc = 8.90 * litros
                print(f'{cauc} litros de gasolina estão custando R${cauc} , carro abastecido')
        
        
carro1 = Carro
        
    