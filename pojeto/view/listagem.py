import tkinter as tk
from tkinter import ttk
from pojeto.controler.cadastrarPC import CadastrarPC


class Listagem(tk.Frame):


    def abrirListagem(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.set_widgets()

    def set_widgets(self):
        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('Nome', 'Data de validade', 'Preço', 'Quantidade')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings')
        self.tree.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        # Barras de rolagem
        ysb = ttk.Scrollbar(orient=tk.VERTICAL, command=self.tree.yview)
        xsb = ttk.Scrollbar(orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree['yscroll'] = ysb.set
        self.tree['xscroll'] = xsb.set
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        xsb.grid(row=1, column=0, sticky=tk.E + tk.W)

        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        # Dados:

        self.data = [

            ('batata', '02/11/2000', '1', '2'),
            ('ovo', '11/09/2001', '1', '2')

        ]

        for item in self.data:
            self.tree.insert('', 'end', values=item)

if __name__ == '__main__':
    root = tk.Tk()

    app = Listagem(master=root)
    app.mainloop()