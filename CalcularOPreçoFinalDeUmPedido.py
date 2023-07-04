valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

# Cálculo do preço final do pedido
precoHamburguer = valorHamburguer * quantidadeHamburguer
precoBebida = valorBebida * quantidadeBebida
precoTotal = precoHamburguer + precoBebida

# Cálculo do troco
troco = valorPago - precoTotal

# Impressão da saída
print(f"O preço final do pedido é R$ {precoTotal:.2f}. Seu troco é R$ {troco:.2f}.")
