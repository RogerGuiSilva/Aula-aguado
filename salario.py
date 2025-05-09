nome = input("Digite seu nome: ")
salario1 = float(input("seu salário de Janeiro: "))
salario2 = float(input(" seu salário de Fevereiro: "))
salario3 = float(input(" seu salário de Março: "))

total = salario1 + salario2 + salario3

print(f"Estimado(a) {nome}. Neste ano você recebeu R$ {total:.2f}.")