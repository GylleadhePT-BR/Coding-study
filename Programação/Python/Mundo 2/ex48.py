print('{:=^60}'.format('TABUADA'))
num = int(input('Digite um numero para ver sua tabuada : '))
for c in range (0,11):
    print('{} x {} = {}'.format(num,c,num*c))
print('~~'*60)