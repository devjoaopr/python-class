class Planta:
    viveiro = "Viveiro verde"
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def valor_total(self):
        return self.preco * self.quantidade
    
    def exibir(self):
        total = self.valor_total()
        print (f"{self.nome} - R$ {self.preco:.2f} X {self.quantidade} = R$ {total:.2f}")
        

plantas = []

def calcular_total(plantas):
    total = 0
    for planta in plantas:
        total =+ planta.valor_total()
    return total

while True:
    inicio = input("digite iniciar para começar a cadastrar plantas ou sair para sair ")
    if inicio == 'sair':
        break
    nome = input("digite o nome da planta ")
    preco = float(input("digite o preço da planta "))
    quantidade = int(input("digite a quantidade "))
    if (quantidade <= 0):
        print("não é permitido cadastrar 0 plantas")

    plantas.append(Planta(nome,preco, quantidade))

print ("Viveiro: {}".format(Planta.viveiro))

for planta in plantas:
    planta.exibir()

    total = calcular_total(plantas)
    
print(f"valor total do estoque: {total:.2f}")

with open ("plantas.txt", "w") as archive:
    for planta in plantas:
        archive.write(f "{planta.nome};{planta.preco};{planta.quantidade}")
        
with open ("plantas.txt", "a") as archive:
    archive.write(f"Total {total:.2f}\n")
    
with open ("plantas.txt", "r") as archive:
    print ("conteudo do arquivo")
    print(archive.read)