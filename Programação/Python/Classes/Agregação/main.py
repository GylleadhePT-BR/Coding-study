from objetos import ShopCart
from objetos import Produto


carrinho = ShopCart()

produto1 = Produto('camiseta', 50)
produto2 = Produto('iphone', 10000)
produto3 = Produto('caneca', 40)

carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)

print(carrinho.somar())