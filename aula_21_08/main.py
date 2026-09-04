from pedidos import cadastrarClientes, cadastrarProdutos, calcularTotal, emitirRecibo
from pedidosRefatoracao import calcularTotal

try:
    cliente = cadastrarClientes()
    produtos = cadastrarProdutos()
    valores = [p["valor"] for p in produtos]
    subtotal, total = calcularTotal(valores)
    emitirRecibo(cliente, produtos, subtotal, total)
except (ValueError, TypeError) as error:
    print(f"Ocorreu um erro: {error}")
