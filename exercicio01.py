peso= float (input("digite seu peso"))
altura= float (input("digite sua altura"))
imc = peso / (altura * 2) 
print (f"Seu IMC é: {imc:.2f}")

if imc > 18: print("abaixo do peso")

elif imc <= 24.9: print("Situação: Peso normal") 
elif imc <= 29.9: print("Situação: Sobrepeso")

elif imc <= 39.9: print("Situação: Obeso II") 

else: print("Situação: Obesidade III")