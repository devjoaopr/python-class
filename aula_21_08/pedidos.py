def cadastrar_clientes():
    telefone = input("Insira o telefone do cliente:")
    endereco = input("Insira o enderero do cliente:")
    nome = input("Insira o nome do cliente:")
    return {"nome": nome, "telefone": telefone, "endereco": endereco}
