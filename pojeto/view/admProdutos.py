from tkinter import *
from pojeto.controler.cadastrarPC import CadastrarPC
from pojeto.banco.conexao import Conexao
from functools import partial

class Adm:
    def principal(self):
        janelaProdutos = Tk()  # Cria a tela principal

        def buscar():
            buscar = CadastrarPC(edProduto.get(),edData.get(),edPreco.get(),edQuantidade.get())
            existe = buscar.existeP()
            select = buscar.selectP()
            if existe:
                # Função do bt buscar(Pesquisar)
                edProduto['state'] = "normal"
                edPreco['state'] = "normal"
                edPreco.insert(0, select[0][2])
                edQuantidade['state'] = "normal"
                edQuantidade.insert(0, select[0][3])
                btAtualizar['state'] = "normal"
                btExcluir['state'] = "normal"



            else:
                edData['state'] = "normal"
                edQuantidade['state'] = "normal"
                edPreco['state'] = "normal"
                btSalvar['state'] = "normal"

        def btnCadastrar():
            cadastrar = CadastrarPC(edProduto.get(),edData.get(),edPreco.get(),edQuantidade.get())
            cadastrado = cadastrar.cadastrarP()
            if cadastrado:
                lbMensagem = Label(janelaProdutos, text="Produto Cadastrado", font=fonte)
                lbMensagem.place(x=20, y=280)
                lbMensagem.grid(row=5, column=1)
            else:
                lbMensagem = Label(janelaProdutos, text="Cadastrado com sucesso", font=fonte)
                lbMensagem.place(x=20, y=280)
                lbMensagem.grid(row=5, column=1)


        def btnDelete():
             delete = CadastrarPC(edProduto.get(),edData.get(),edPreco.get(),edQuantidade.get())
             delete = delete.deleteP()
             return delete

        def btnUpdate():
            update = CadastrarPC(edProduto.get(),edData.get(),edPreco.get(),edQuantidade.get())
            update = update.atualizaP()
            return update





            # Cria a tela principal
        quadro = Frame(janelaProdutos, bd=2, relief="raised", pady=10, padx=10)
        quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
        fonte = ('Arial', '16', 'bold')  # Define o padrão de fonte

    #FORMULARIO


        lbProduto = Label(quadro, text="Produto:", font=fonte, pady=10, padx=10)
        lbData = Label(quadro, text="Data de validade:", font=fonte, pady=10, padx=10)
        lbQuantidade = Label(quadro, text="Quantidade:", font=fonte, pady=10, padx=10)
        lbPreco = Label(quadro, text="Preço:", font=fonte, pady=10, padx=10)
        edProduto = Entry(quadro, font=fonte, width=25)
        edData = Entry(quadro, font=fonte, width=25, state="disabled")
        edQuantidade = Entry(quadro, font=fonte, width=25, state="disabled")
        edPreco = Entry(quadro, font=fonte, width=25, state="disabled")

        btSalvar = Button(quadro, font=fonte, text="Salvar", fg="Blue", state="disabled",
        activebackground="#A9A9A9", activeforeground="white") #command=btSalvar
        btSalvar["command"] = partial(btnCadastrar)
        btAtualizar = Button(quadro, font=fonte, text="Atualizar", fg="green", state="disabled",
                              activebackground="#ff8000", activeforeground="white")
        btAtualizar["command"] = partial(btnUpdate)
        btExcluir = Button(quadro, font=fonte, text="Excluir", fg="red", state="disabled",
                              activebackground="#ff8000", activeforeground="white")
        btExcluir["command"] = partial(btnDelete)
        #EXIBINDO OS ITENS CARAI


        lbProduto.grid(row=0, column=0)
        edProduto.grid(row=0, column= 1)
        lbData.grid(row=1, column=0)
        edData.grid(row=1, column= 1)
        lbQuantidade.grid(row=2, column=0)
        edQuantidade.grid(row=2, column= 1)
        lbPreco.grid(row=3, column=0)
        edPreco.grid(row=3, column= 1)
        btSalvar.grid(row=4, column=0)
        btAtualizar.grid(row=4, column=1)
        btExcluir.grid(row=4, column=2)



        photoLupa = PhotoImage(file="../img/lupa.png")
        logoLupa = photoLupa.subsample(15, 15)
        btBusca = Button(quadro, bd=0, image=logoLupa)
        btBusca["command"] = partial(buscar)
        btBusca.grid(row=0, column=2)

            # criando lb mensagem
        lbMensagem = Label(janelaProdutos, text="", font=fonte)
        lbMensagem.place(x=20, y=280)

        # Configurações da janela

        quadro = Frame(janelaProdutos, relief="raised", pady=10, padx=10)
        quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
        fonte = ('Arial', '16', 'bold')

        janelaProdutos.geometry("640x320+200+200")  # Larg x Alt + DistaciaEsq + DistandiaTop
        janelaProdutos.title("Consulta, Cadastro e Alteração")  # Define o titulo da janela
        #janela.iconbitmap("img/icone.ico")
        janelaProdutos.mainloop()  # Exibe a janela

