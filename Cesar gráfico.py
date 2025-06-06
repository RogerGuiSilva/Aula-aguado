import tkinter as tk
from tkinter import ttk, messagebox

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

def executar():
    modo = modo_var.get()
    try:
        chave = int(chave_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "A chave deve ser um número inteiro.")
        return

    mensagem = mensagem_entry.get("1.0", tk.END).strip()
    if modo == "Criptografar":
        resultado = criptografa(mensagem, chave)
    else:
        resultado = descriptografa(mensagem, chave)

    resultado_entry.config(state='normal')
    resultado_entry.delete("1.0", tk.END)
    resultado_entry.insert(tk.END, resultado)
    resultado_entry.config(state='disabled')

janela = tk.Tk()
janela.title("Cifra de César - Criptografia")

frame = ttk.Frame(janela, padding=20)
frame.grid()

modo_var = tk.StringVar(value="Criptografar")
ttk.Label(frame, text="Modo:").grid(column=0, row=0, sticky="w")
ttk.Radiobutton(frame, text="Criptografar", variable=modo_var, value="Criptografar").grid(column=1, row=0, sticky="w")
ttk.Radiobutton(frame, text="Descriptografar", variable=modo_var, value="Descriptografar").grid(column=2, row=0, sticky="w")

ttk.Label(frame, text="Chave:").grid(column=0, row=1, sticky="w")
chave_entry = ttk.Entry(frame, width=5)
chave_entry.grid(column=1, row=1, sticky="w")

ttk.Label(frame, text="Mensagem:").grid(column=0, row=2, columnspan=3, sticky="w", pady=(10, 0))
mensagem_entry = tk.Text(frame, width=50, height=5)
mensagem_entry.grid(column=0, row=3, columnspan=3)

executar_btn = ttk.Button(frame, text="Executar", command=executar)
executar_btn.grid(column=0, row=4, pady=10)

ttk.Label(frame, text="Resultado:").grid(column=0, row=5, columnspan=3, sticky="w", pady=(10, 0))
resultado_entry = tk.Text(frame, width=50, height=5, state='disabled')
resultado_entry.grid(column=0, row=6, columnspan=3)

janela.mainloop()