from Classes import *

pontoa = float(input('Digite o ponto A do triangulo : '))
pontob = float(input('Digite o ponto B do triangulo : '))
pontoc = float(input('Digite o ponto C do triangulo : '))

t1 = Triangulo(pontoa, pontob, pontoc)
t1.perimetro()