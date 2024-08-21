import tkinter as tk

class UsuarioForm:
    def __init__(self, Master):
        self.master = Master
        Master.title('Formulários de Usuários')

        self.label_nome = tk.Label(Master, text="Nome:")
        self.label_nome.grid(row=0 column=0, padx=10, pady=10)

        self.entry_nome = tk.Entry(Master)
        self.entry_nome.grid(row=0, columan=1, padx=10, pady=10)

        self.label_email = tk.Label(Master, text="E-mail:")
        self.label_email.grid(row=1, column=0, padx=10, pady=10)

        self.entry_email = tk.Entry(Master)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        self.label_telefone = tk.Label(Master, text="telefone")
        self.label_telefone.grid(row=2, column=0, padx=10, pady=10)

        self.entry_telefone = tk.Entry(Master)
        self.entry_telefone.grid(row=2, column=1, padx=10, pady=10)

        self.botao_enviar = tk.Button(Master,text="enviar",
    command=self.enviar_formulario)
        self.botao_enviar.grid(row=3, column=0, padx=10, pady=10)

    def enviar_formulario(self):
            nome = self.entry_nome.get()
            email = self.entry_email.get()
            telefone = self.entry_telefone.get()

            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Telefone: {telefone}')

            self.entry_nome.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)

root = tk.Tk()
app = UsuarioForm(root)
root.mainloop()