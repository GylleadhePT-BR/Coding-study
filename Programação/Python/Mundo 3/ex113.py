def leiaint(num):
    while True :
        try:
            n = int(input(num))
        except(ValueError,TypeError):
            print('\033[0;0;31mERRO!!, por favor digite um valor válido...\033[m')
            continue
        else:
            return n
def leiafloat(num):
    while True:
        try:
            n = float(input(num))
        except(ValueError,TypeError):
            print('\033[0;0;31mERRO!! , por favor digite um valor válido..\033[m')
            continue
        else:
            return n



n1 = leiaint('Digite um valor inteiro : ')
n2 = leiafloat('Digite um valor real :')