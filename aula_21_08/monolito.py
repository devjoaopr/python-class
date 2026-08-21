telefone = input("Insira o telefone do cliente:")
endereco = input("Insira o enderero do cliente:")
nome = input("Insira o nome do cliente:")

print("=== Produtos do pedido ===")
produto = []
valores = []

while True:
    fim = input("Nome do produto produto (ou digite 'fim' para encerrar):")
    if fim == "fim":
        break
    valor = float(input(f"valor de {produto}"))
    valores.append(valor)

    subtotal = 0
    for v in valores:
        subtotal = subtotal + v

    desconto = input(float("insira o valor do desconto em %"))
    subtotalComDesconto = subtotal - (subtotal * desconto / 100)
    total = subtotalComDesconto + 5.0  # taxa de frete

    print("=== Recibo ===")
    print(f"Cliente: {nome} / telefone: {telefone}")
    print(f"Endereço {endereco}")

    for i in range(len(produto)):
        print(f"{produto[i]} - R$ {valores[i]}")
    print(f"subtotal: R${round(subtotal, 2)}")
