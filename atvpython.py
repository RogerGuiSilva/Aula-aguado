nome = input("digite seu nome")
anoC = int(input("digite o ano do seu carro"))

if anoC < 1995:
    print(f"Parabens {nome}. seu carro é um classico")

elif 1996 <= anoC <= 2005:
   print(f"Parabens{nome}. pelo menos seu carro não tem mais IPVA")

else:
    print("seu carro é novo ainda")


