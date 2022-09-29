
from time import sleep
def contador(inicio , fim , passo):
    print(f'Contando de {inicio} até {fim} pulando de {passo} em {passo}.')
    sleep(1.5)
    if passo < 0:
        passo += 1
    if inicio < fim:
        cont  = inicio
        while cont <= fim :
            sleep(0.5)
            print(f' {cont}',end='')
            cont+= passo
        print(' FIM')
    else:
        cont = inicio
        while cont >= fim :
            sleep(0.5)
            print(f' {cont}',end='')
            cont -= passo
        print(' FIM')

contador(1,10,1)
contador(10,1,1)
print('Agora personalize sua contagem...')
i = int(input('Incio : '))
f = int(input('Fim :  '))
p = int(input('Passo : '))
contador(i,f,p)