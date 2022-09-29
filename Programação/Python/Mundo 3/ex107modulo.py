
def l(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)

def moeda(num):
    return (f'R${num:.2f}')


def dobro(num):
    x = num * 2
    return x
def metade(num):
    m = num / 2
    return m
def aumento(num,porcet):
   ml = (porcet / 100) + 1
   r = ml * num
   return r


