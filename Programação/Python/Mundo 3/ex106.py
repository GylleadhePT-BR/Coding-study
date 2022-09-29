from time import sleep
from datetime import date

def l(txt,cor=0):
    tam = len(txt) + 4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {txt}')
    print('~'*tam)
    print(c[0],end='')


l('CADASTRO PESSOAL',2)
sleep(1)
l('SEJA BEM VINDO(a) AO NOSSO HOSPITAL..',1)
sleep(1)
l('VAMOS INICIAR O CADASTRO',1)
print('-'*30)
sleep(1)
princ = []
ex = 'S'
while ex == 'S':
    princ.append(str(input('Nome :')))
    princ.append(int(input('idade :')))
    ex = str(input('\033[1;30;43mDeseja continuar ? [S/N] : \033[m')).strip().upper()
if ex == 'N':
    sleep(1)
    l('As pessoas foram cadastradas com Sucesso!!',2)
    sleep(1)
    l('OBRIGADO POR USAR NOSSO SISTEMA ATÈ LOGO...',2)





