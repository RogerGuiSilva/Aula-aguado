listacarro= []

for i in range(3):
    print(f"\nCadastro do {i+1}º carro:")
    nome = input("Digite o nome do carro: ")
    ano = input("Digite o ano do carro: ")
    motor = input("Digite o tipo de motor do carro: ")
    
    carro = [nome, ano, motor]
    listacarro.append(carro)

print("\nCarro cadastrados:")
for i in range(len(listacarro)):
    print(f"Nome: {listacarro[i][0]}, Ano: {listacarro[i][1]}, Motor: {listacarro[i][2]}")
