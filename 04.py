
temperaturas = {
    "Domingo": 27,
    "Segunda": 30,
    "Terça": 27.6,
    "Quarta": 23.5,
    "Quinta": 29.3,
    "Sexta": 24,
    "Sábado": 21
}

valores = list(temperaturas.values())
media = sum(valores) / len(valores)

print("A menor temperatura foi", min(valores))
print("A maior temperatura foi", max(valores))

print("\nTemperaturas abaixo da média ({:.2f}):".format(media))
for dia, temp in temperaturas.items():
    if temp < media:
        print(dia, ":", temp)
