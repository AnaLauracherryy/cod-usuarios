import tkinter as tk
from tkinter import  messagebox

def mostrar_usuarios():
    messagebox.showinfo("usuários","botão usuários clicado!")

def mostrar_cidades():
    messagebox.showinfo("cidades","botão cidades clicado!")

def mostrar_clientes():
    messagebox.showinfo("clientes","botão clientes clicado!")

def fechar_aplicacao():
    root.quit()

root = tk.Tk()
root.title("Página Principal")
root.geometry("500x200")

btn_usuarios = tk.Button(root, text="Usuarios", command=mostrar_usuarios)
btn_usuarios.pack(pady=10)

btn_cidades = tk.Button(root, text="cidades", command=mostrar_cidades)
btn_cidades.pack(pady=10)

btn_clientes = tk.Button(root, text="clientes", command=mostrar_clientes)
btn_clientes.pack(pady=10)

btn_fechar = tk.Button(root, text="fechar", command=fechar_aplicacao)
btn_fechar.pack(pady=10)

root.mainloop()