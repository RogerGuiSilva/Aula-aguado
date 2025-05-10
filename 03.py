dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
todas_temperaturas = []


for semana in range(1, 4):
    print("\nSemana", semana)
    semana_temp = []
    for dia in dias:
        valor = float(input(f"Digite a temperatura de {dia}: "))
        semana_temp.append(valor)
    todas_temperaturas.append(semana_temp)


soma = 0
total = 0
for semana in todas_temperaturas:
    for temp in semana:
        soma += temp
        total += 1

media = soma / total

# Mostrar abaixo da média
print("\nTemperaturas abaixo da média ({:.2f}):".format(media))
for i in range(3):
    for j in range(7):
        if todas_temperaturas[i][j] < media:
            print(f"Semana {i+1} - {dias[j]}: {todas_temperaturas[i][j]}")
