larg = float(input("Qual a largura da parede ?"))
alt = float(input("Qual a altura da parede ?"))
area = larg * alt
tinta = area/2
print('A sua parede com dimensões de {}x{},tem área de {} ,e será preciso {:.2}L de tinta para pinta-la totalmente.'.format(larg,alt,area,tinta))