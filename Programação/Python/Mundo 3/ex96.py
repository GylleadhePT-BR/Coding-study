def l(txt):
    tam = len(txt)
    print('~'*tam)
    print(txt)
    print('~'*tam)


l('Controlador de Terrenos')

def area(largura , comprimento):
    print(f'Um terro com comprimento de {largura}m e largura de {comprimento}m tem area de {cp*lg}')


print('Nos informe as dimensões : ')
cp = float(input('Comprimento : '))
lg = float(input('Largura : '))
area(lg,cp)