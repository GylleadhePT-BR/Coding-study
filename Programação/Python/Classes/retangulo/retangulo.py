class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def cauculaArea(self):
        return self.base * self.altura

    def caucularPerimetro(self):
        return 2*self.base + 2*self.altura
    
retangulo1 = Retangulo(int(input('Digite o valor')),int(input('Diite outro valor:')))
print(retangulo1.cauculaArea())