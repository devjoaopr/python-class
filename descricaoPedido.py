def descrever_pedido(cliente, **extras):
    print("Clientes: ", cliente)
    for chave, valor in extras.items():
        print(f" {chave} - {valor}")


dados = {"observacao": "Sem cebola", "retirada": False}
cliente = "Ana"
descrever_pedido(cliente, **dados)
