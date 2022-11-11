class Triangulo():
    def __init__(self , a , b , c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        p = self.a + self.b + self.c
        print(f'O perimetro do seu triangulo é iogual a : {p}')
        
        
    def Area(self):
        area = (self.b*self.a)/ 2
        print(f'A area do triangulo informado é igual a {area}')
        
        

        