from pojeto.controler.cadastrarC import Cadastrar
from tkinter import *
from functools import partial

class CadastraUsuario:

    def abrirCadastro():
        janela = Tk()  # Cria a tela principal
        janela.resizable(0, 0)
        quadro = Frame(janela, bd=2, relief="raised", pady=10, padx=10)
        quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
        fonte = ('Arial', '16', 'bold')  # Define o padrão de fonte

        def cadastrarUser():
            cadastrar = Cadastrar(edNome.get(), edSenha.get(),edEmail.get())
            cadastrado = cadastrar.cadastrarC()

            if cadastrado:
                lbMensagem = Label(janela, text="Cadastrado com sucesso", font=fonte)
                lbMensagem.place(x=20, y=280)
                lbMensagem.grid(row=5, column=1)
                janela.destroy()
            else:
                lbMensagem = Label(janela, text="Usuario Já cadastrado antes", font=fonte)
                lbMensagem.place(x=20, y=280)
                lbMensagem.grid(row=5, column=1)


        # Criando os componentesdo formulario
        lbNome = Label(quadro, text="Nome:", font=fonte, pady=10, padx=10)
        lbEmail = Label(quadro, text="E-mail:", font=fonte, pady=10, padx=10)
        lbSenha = Label(quadro, text="Senha:", font=fonte, pady=10, padx=10)
        edNome = Entry(quadro, font=fonte, width=25)
        edEmail = Entry(quadro, font=fonte, width=25)
        edSenha = Entry(quadro, font=fonte, width=25)
        btSalvar = Button(quadro, font=fonte, text="Salvar", fg="Blue",
        activebackground="#A9A9A9", activeforeground="white" )
        btSalvar["command"] = partial(cadastrarUser)


        # Exibindo os componentes do formulario com grid
        lbNome.grid(row=2, column=0)
        lbEmail.grid(row=1, column=0)
        lbSenha.grid(row=3, column=0)
        edNome.grid(row=2, column=1)
        edSenha.grid(row=3, column=1)
        edEmail.grid(row=1, column=1)
        btSalvar.grid(row=4, column=1)



        # criando o botão de busca
        #photoLupa = PhotoImage(file="img/lupa2.png")
        #logoLupa = photoLupa.subsample(15, 15)


        # criando lb mensagem


        # Configurações da janela
        janela.geometry("540x320+200+200")  # Larg x Alt + DistaciaEsq + DistandiaTop
        janela.title("CADASTRO")  # Define o titulo da janela
        #janela.iconbitmap("img/icone.ico")
        janela.mainloop()  # Exibe a janela
