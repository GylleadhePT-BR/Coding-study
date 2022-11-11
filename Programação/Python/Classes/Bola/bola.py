class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mudarCor(self):
        if self.cor == '':
            print('ERRO!! , ainda nao oi adicinada nenhuma cor')
            self.cor = input('Digite uma cor para a bola  : ')
        else:
            self.cor = input('Digite uma cor para a bola  : ')
            print(f"Nova cor adicionada foi {self.cor}")

    def mostrarCor(self):
        print(self.cor)
