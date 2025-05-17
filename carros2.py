listacarro = []

for i in range(3):
    print(f"\nCadastro do {i+1}º carro:")
    nome = input("Digite o nome do carro: ")
    ano = input("Digite o ano do carro: ")
    motor = input("Digite o tipo de motor do carro: ")
    
    carro = {"nome": nome, "ano": ano, "motor": motor}
    listacarro.append(carro)

print("\nCarros cadastrados:")
for carro in listacarro:
    print(f"Nome: {carro['nome']}, Ano: {carro['ano']}, Motor: {carro['motor']}")


resposta = input("\nDeseja excluir algum carro? (s/n): ")
if resposta.lower() == "s":
    excluir = input("Digite o nome do carro que deseja excluir: ")
    for carro in listacarro:
        if carro["nome"].lower() == excluir.lower():
            listacarro.remove(carro)
            print("Carro apagado!")
            break
    else:
        print("vixi não tenho esse carro.")

print("\ncarros armazenados:")
for carro in listacarro:
    print(f"Nome: {carro['nome']}, Ano: {carro['ano']}, Motor: {carro['motor']}")
