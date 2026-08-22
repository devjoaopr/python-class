def cadastrarClientes():
    telefone = input("Insira o telefone do cliente:")
    endereco = input("Insira o enderero do cliente:")
    nome = input("Insira o nome do cliente:")
    return {"nome": nome, "telefone": telefone, "endereco": endereco}


def cadastrarProdutos():
    produtos = []

    while True:
        produto = input("Nome do produto (ou digite 'fim' para encerrar):")
        if produto == "fim":
            break
        valor = float(input(f"valor de {produto}"))
        produtos.append({"nome": produto, "valor": valor})
    return produtos


def calcularTotal(valores):
    subtotal = sum(valores)
    taxaEntrega = 5.0
    total = subtotal + taxaEntrega
    return subtotal, total


def emitirRecibo(cliente, produtos, subtotal, total):
    print("=== Recibo ===")
    print(f"Cliente: {cliente['nome']} - {cliente['telefone']}")
    print(f"Endereço: {cliente['endereco']}")
    for p in produtos:
        print(f" - {p['nome']}: R$ {p['valor']:.2f}")
    print(f"subtotal: {subtotal:.2f}")
    print(f"total a pagar = {total:.2f}")


cliente = cadastrarClientes()
produtos = cadastrarProdutos()
valores = [p["valor"] for p in produtos]
subtotal, total = calcularTotal(valores)
emitirRecibo(cliente, produtos, subtotal, total)
