from datetime import datetime


valor = float(input("Digite o valor da compra: R$ "))
nasc = input("Informe sua data de nascimento (dia/mes/ano): ")
socio = input("Você é sócio do Clube (S/N): ").upper()

data_nascimento = datetime.strptime(nasc, "%d/%m/%Y")
hoje = datetime.today()

idade = hoje.year - data_nascimento.year
if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

aniversario_mes = hoje.month == data_nascimento.month

desconto = 0

if idade > 60 or socio == "S":
    desconto += 10

if socio == "S" and aniversario_mes:
    desconto += 5

valor_final = valor * (1 - desconto / 100)

print(f"Valor final da compra: R$ {valor_final:.2f}")
