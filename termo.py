import tkinter as tk

def mostrar_letras():
    texto.delete("1.0", tk.END)
    palavra = entrada.get()
    for letra in palavra:
        texto.insert(tk.END, letra + "\n")

janela = tk.Tk()
janela.title("Separar Letras")

instrucao = tk.Label(janela, text="Digite uma palavra:")
instrucao.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Mostrar Letras", command=mostrar_letras)
botao.pack(pady=10)

texto = tk.Text(janela, height=10, width=30)
texto.pack()

janela.mainloop()