from objetos import Escritor
from objetos import Caneta
from objetos import MaquinaEscrever

esc1 = Escritor('Joao', '12')
maquina1 = MaquinaEscrever('philips')
caneta1 = Caneta('vermelho', 'bic')

esc1.ferramenta = maquina1
esc1.ferramenta.escrever()