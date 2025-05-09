total = float(input("Digite o valor total da compra: R$"))

idade = int(input("Digite sua idade: "))

socio = input("Você é sócio do Clube Delta? (S/N): ").upper()

aniversario = input("Você está fazendo aniversário esse mês? (S/N): ").upper()
desconto = 0
if idade > 60 or socio == 'S':
    desconto += 10  
if socio == 'S' and aniversario == 'S':
    desconto += 5  


if total >= 100:
    total -= desconto  

print(f"Valor final da compra: R${total:.2f}")
