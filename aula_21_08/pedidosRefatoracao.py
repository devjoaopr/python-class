def calcularTotal(valores, desconto=0.0, taxaDeEntrega=10.0):
    subtotal = sum(valores)
    subtotalComDescontos = subtotal - (subtotal * desconto / 100)
    total = subtotalComDescontos + taxaDeEntrega
    return subtotal, total


desconto = float(input("Digite o valor do desconto em % "))
taxaEntrega = float(input("digite o valor da taxa de entrega "))
total = calcularTotal([10, 20, 35, 60], desconto, taxaEntrega)
print(total)
