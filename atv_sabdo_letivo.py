import tkinter as tk
from tkinter import messagebox

produtos = {}

def adicionar_produto():
    nome = entrada_nome.get().strip()
    preco_str = entrada_preco.get().strip().replace(',', '.')

    if nome == "":
        messagebox.showwarning("Aviso", "Precisa colocar o nome do produto.")
        return

    try:
        preco = float(preco_str)
        produtos[nome] = preco
        atualizar_lista()
        entrada_nome.delete(0, tk.END)
        entrada_preco.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Precisa adicionar o nome do produto.")

def atualizar_lista():
    lista_produtos.delete(0, tk.END)
    for nome, preco in produtos.items():
        lista_produtos.insert(tk.END, f"{nome}: R$ {preco:.2f}")

tl = tk.Tk()
tl.title("Cadastro de Produtos")
tl.geometry("400x400")

tk.Label(tl, text="Nome do Produto:").pack()
entrada_nome = tk.Entry(tl, width=40)
entrada_nome.pack(pady=5)

tk.Label(tl, text="Preço (R$):").pack()
entrada_preco = tk.Entry(tl, width=40)
entrada_preco.pack(pady=5)

tk.Button(tl, text="Adicionar Produto", command=adicionar_produto).pack(pady=10)

tk.Label(tl, text="Produtos Cadastrados:").pack()
lista_produtos = tk.Listbox(tl, width=50)
lista_produtos.pack(pady=10)

tl.mainloop()
