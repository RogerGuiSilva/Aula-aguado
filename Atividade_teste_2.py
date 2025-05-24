
def criptografa(numeros, chave):
    return [num + chave for num in numeros]

def descriptografa(numeros, chave):
    return [num - chave for num in numeros]

def menu():
    
    entrada = input("Digite os números separados por espaço: ")
    numeros = list(map(int, entrada.split()))


    chave = int(input("Digite a chave de criptografia (número inteiro): "))

    
    operacao = input("Deseja criptografar ou descriptografar? (c/d): ").lower()

    if operacao == 'c':
        resultado = criptografa(numeros, chave)
        print("Resultado criptografado:", resultado)
    elif operacao == 'd':
        resultado = descriptografa(numeros, chave)
        print("Resultado descriptografado:", resultado)
    else:
        print("Opção inválida. Use 'c' para criptografar ou 'd' para descriptografar.")


menu()
