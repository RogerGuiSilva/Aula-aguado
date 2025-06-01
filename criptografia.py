def criptografa(mensagem, chave):
    resultado = ''
    for caractere in mensagem:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            deslocado = (ord(caractere) - base + chave) % 26
            resultado += chr(base + deslocado)
        else:
            resultado += caractere
    return resultado

def descriptografa(mensagem, chave):
    return criptografa(mensagem, -chave)

def main():
    while True:
        print("\n=== Cifra de César ===")
        print("1. Criptografar")
        print("2. Descriptografar")
        print("3. Sair")
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == '1':
            mensagem = input("Digite a mensagem para criptografar: ")
            chave = int(input("Digite a chave de criptografia (número inteiro): "))
            criptografada = criptografa(mensagem, chave)
            print(f"Mensagem criptografada: {criptografada}")
        elif opcao == '2':
            mensagem = input("Digite a mensagem para descriptografar: ")
            chave = int(input("Digite a chave de descriptografia (número inteiro): "))
            descriptografada = descriptografa(mensagem, chave)
            print(f"Mensagem descriptografada: {descriptografada}")
        elif opcao == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
