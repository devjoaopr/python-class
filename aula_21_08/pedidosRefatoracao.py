def calcularTotal(valores, desconto=0.0, taxaDeEntrega=10.0):
    subtotal = sum(valores)
    subtotalComDescontos = subtotal - (subtotal * desconto / 100)
    total = subtotalComDescontos + taxaDeEntrega
    return subtotal, total


desconto = float(input("Digite o valor do desconto em %"))
calcularTotal()
