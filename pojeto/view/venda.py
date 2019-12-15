from tkinter import *
from pojeto.banco.conexao import Conexao
from pojeto.controler.cadastrarVC import CadastrarVC
from functools import partial




class Vendas:
    def abrirVendas(self):
        janela = Tk()  # Cria a tela principal
        janela.resizable(0, 0)
        quadro = Frame(janela, bd=2, relief="raised", pady=10, padx=10)
        quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
        fonte = ('Arial', '16', 'bold')  # Define o padrão de fonte


        def btnVendas():
            cadastrar = CadastrarVC(edProduto.get(), edVender.get(), edInvisivel.get(), edFranquia.get())
            cadastrado = cadastrar.CadastrarVenda()
            return cadastrado


#FORMULARIO


        lbProduto = Label(quadro, text="Produto:", font=fonte, pady=10, padx=10)
        lbVender = Label(quadro, text="Vender:", font=fonte, pady=10, padx=10)
        lbFranquia = Label(quadro, text="Franquia:", font=fonte, pady=10, padx=10)
        edProduto = Entry(quadro, font=fonte, width=25)
        edInvisivel = Entry(quadro, font=fonte, width=25, text='7')
        edVender = Entry(quadro, font=fonte, width=25)
        edFranquia = Entry(quadro, font=fonte, width=25)


        btVenda = Button(quadro, font=fonte, text="Vender", fg="green",
        activebackground="#A9A9A9", activeforeground="white")
        btVenda['command'] = partial(btnVendas)


        #EXIBINDO OS ITENS


        lbProduto.grid(row=0, column=0)
        edProduto.grid(row=0, column=1)
        lbVender.grid(row=2, column=0)
        edVender.grid(row=2, column=1)
        lbFranquia.grid(row=3, column=0)
        edFranquia.grid(row=3, column=1)



        btVenda.grid(row=5, column=1)




        #photoLupa = PhotoImage(file="img/lupa2.png")
        #logoLupa = photoLupa.subsample(15, 15)
        btBusca = Button(quadro, bd=1) #image=logoLupa
        btBusca.grid(row=0, column=3)

        # criando lb mensagem
        lbMensagem = Label(janela, text="", font=fonte)
        lbMensagem.place(x=20, y=280)


        janela.geometry("640x320+200+200")  # Larg x Alt + DistaciaEsq + DistandiaTop
        janela.title("Consulta, Cadastro e Alteração")  # Define o titulo da janela
        #janela.iconbitmap("img/icone.ico")
        janela.mainloop()  # Exibe a janela

