from pedidos import cadastrarClientes, cadastrarProdutos, emitirRecibo
from pedidosRefatoracao import calcularTotal
from descricaoPedido import descrever_pedido

try:
    """Cadastrar cliente e produtos"""
    cliente = cadastrarClientes()
    produtos = cadastrarProdutos()

    """ Calcular subtotal e total do pedido, descrever o pedido e emitir o recibo """
    valores = [p["valor"] for p in produtos]
    subtotal, total = calcularTotal(valores)

    """ Descrever o pedido """
    descrever_pedido(cliente, produtos=produtos, subtotal=subtotal, total=total)

    """ Emitir recibo do pedido"""
    emitirRecibo(cliente, produtos, subtotal, total)

except (ValueError, TypeError) as error:
    print(f"Ocorreu um erro: {error}")
