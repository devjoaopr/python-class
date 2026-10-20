class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome}, minha idade é {self.idade}")


pessoa1 = Pessoa("joao", 18)
rodar = pessoa1.apresentar()


class ArquivoPessoa:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def adicionar(self, pessoa):
        with open(self.nome_arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{pessoa.nome};{pessoa.idade}\n")

    def exibir(self):
        with open(self.nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, idade = linha.strip().split(";")
                print(f"Nome: {nome} | Idade: {idade}")


arquivo = ArquivoPessoa("listaNomes.txt")

while True:
    nome = input("digite seu nome, ou digite sair para sair ")
    if nome == "sair":
        break
    idade = input("digite sua idade ")

    pessoa = Pessoa(nome, idade)
    arquivo.adicionar(pessoa)
arquivo.exibir()
