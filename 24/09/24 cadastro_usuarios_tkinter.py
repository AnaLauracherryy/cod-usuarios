
usuarios = {}

def incluir_usuario():
    usuario_id = input("Digite o ID do usuário: ")
    if usuario_id in usuarios:
        print("Usuário já cadastrado.")
    else:
        nome = input("Digite o nome do usuário: ")
        idade = input("Digite a idade do usuário: ")
        usuarios[usuario_id] = {'nome': nome, 'idade': idade}
        print("Usuário cadastrado com sucesso!")

def alterar_usuario():
    usuario_id = input("Digite o ID do usuário que deseja alterar: ")
    if usuario_id in usuarios:
        nome = input("Digite o novo nome do usuário: ")
        idade = input("Digite a nova idade do usuário: ")
        usuarios[usuario_id] = {'nome': nome, 'idade': idade}
        print("Usuário alterado com sucesso!")
    else:
        print("Usuário não encontrado.")

def excluir_usuario():
    usuario_id = input("Digite o ID do usuário que deseja excluir: ")
    if usuario_id in usuarios:
        del usuarios[usuario_id]
        print("Usuário excluído com sucesso!")
    else:
        print("Usuário não encontrado.")

def listar_usuarios():
    if usuarios:
        print("Usuários cadastrados:")
        for usuario_id, dados in usuarios.items():
            print(f"ID: {usuario_id}, Nome: {dados['nome']}, Idade: {dados['idade']}")
    else:
        print("Nenhum usuário cadastrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Incluir usuário")
        print("2. Alterar usuário")
        print("3. Excluir usuário")
        print("4. Listar usuários")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            incluir_usuario()
        elif opcao == '2':
            alterar_usuario()
        elif opcao == '3':
            excluir_usuario()
        elif opcao == '4':
            listar_usuarios()
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário para armazenar os usuários
usuarios = {}

def incluir_usuario():
    usuario_id = id_entry.get()
    if usuario_id in usuarios:
        messagebox.showerror("Erro", "Usuário já cadastrado.")
    else:
        nome = nome_entry.get()
        idade = idade_entry.get()
        usuarios[usuario_id] = {'nome': nome, 'idade': idade}
        atualizar_treeview()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

def alterar_usuario():
    usuario_id = id_entry.get()
    if usuario_id in usuarios:
        nome = nome_entry.get()
        idade = idade_entry.get()
        usuarios[usuario_id] = {'nome': nome, 'idade': idade}
        atualizar_treeview()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Usuário alterado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.")

def excluir_usuario():
    usuario_id = id_entry.get()
    if usuario_id in usuarios:
        del usuarios[usuario_id]
        atualizar_treeview()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.")

def atualizar_treeview():
    for i in treeview.get_children():
        treeview.delete(i)
    for usuario_id, dados in usuarios.items():
        treeview.insert('', 'end', values=(usuario_id, dados['nome'], dados['idade']))

def limpar_campos():
    id_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    idade_entry.delete(0, tk.END)

def selecionar_usuario(event):
    selecionado = treeview.focus()
    if selecionado:
        usuario_id = treeview.item(selecionado)['values'][0]
        dados = usuarios[usuario_id]
        id_entry.delete(0, tk.END)
        id_entry.insert(0, usuario_id)
        nome_entry.delete(0, tk.END)
        nome_entry.insert(0, dados['nome'])
        idade_entry.delete(0, tk.END)
        idade_entry.insert(0, dados['idade'])

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Usuários")

# Campos do formulário
tk.Label(root, text="ID do Usuário:").grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

tk.Label(root, text="Nome:").grid(row=1, column=0)
nome_entry = tk.Entry(root)
nome_entry.grid(row=1, column=1)

tk.Label(root, text="Idade:").grid(row=2, column=0)
idade_entry = tk.Entry(root)
idade_entry.grid(row=2, column=1)

# Botões
tk.Button(root, text="Incluir", command=incluir_usuario).grid(row=3, column=0)
tk.Button(root, text="Alterar", command=alterar_usuario).grid(row=3, column=1)
tk.Button(root, text="Excluir", command=excluir_usuario).grid(row=3, column=2)

# Treeview
treeview = ttk.Treeview(root, columns=("ID", "Nome", "Idade"), show="headings")
treeview.heading("ID", text="ID")
treeview.heading("Nome", text="Nome")
treeview.heading("Idade", text="Idade")
treeview.grid(row=4, column=0, columnspan=3)

# Evento de seleção no Treeview
treeview.bind("<<TreeviewSelect>>", selecionar_usuario)

# Executa o loop da interface
root.mainloop()
