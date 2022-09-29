cont= ('zero','um','dois','tres','quatro','cinco',
        'seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quize',
        'dezesseis','dezessete','dezoite','dezenove','vinte')
resp = 'S'
while resp == 'S':
    num = int(input('Digite um numero entre 0 e 20 : '))
    if 0 <= num <= 20:
        print(f'você digitou o numero {cont[num]}')
    resp = str(input('Deseja continuar ? [N/S]')).strip().upper()
if resp == 'N':
    print('Obrigado por usar o nosso programa..')

