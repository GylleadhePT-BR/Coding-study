preço = float(input("Qual o preço do produto ?"))
desconto = int(input("Quanto de desconto deseja aplicar ?"))
cauculo = (100-desconto)/100
c2 = cauculo*preço
print("O produto que custava R${:.2} agora com desconto de {:.2}%, custará R${:.2}".format(preço,desconto,c2))