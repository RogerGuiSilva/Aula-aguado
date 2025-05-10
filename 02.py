dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
temperaturas = [27, 30, 27.6, 23.5, 29.3, 24, 21]

soma = sum(temperaturas)
media = soma / len(temperaturas)

print("Temperaturas abaixo da média ({:.2f}):".format(media))

for i in range(7):
    if temperaturas[i] < media:
        print(dias[i], ":", temperaturas[i])
