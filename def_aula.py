
def ordenar(vet):
    for i in range(0, len(vet)-1):
        r = 0
        while r < len(vet)-1-i:
            if vet[r] > vet[r+1]:
                troca = vet[r+1]
                vet[r+1] = vet[r]
                vet[r] = troca
            r += 1
    return vet

vet = []

for i in range(0, 5):
    resp = int(input(f"Digite o número {i+1}: "))
    vet.append(resp)

vet = ordenar(vet)
print(vet)
