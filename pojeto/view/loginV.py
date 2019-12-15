from tkinter import *
from pojeto.controler.LoginC import LoginC
from functools import partial
from pojeto.view.home import Home
from pojeto.view.cadastrarUserV import CadastraUsuario

class LoginView():
    def MainLogin(self):
        janela = Tk()  # Cria a tela principal

        def exibeM():
            return lblMensagem.grid(row=3, column=1)

        def btnLogin():
            loginC = LoginC(edLogin.get(), edSenha.get())
            verific = loginC.verificar()
            if verific:
                janela1 = Home()
                janela.destroy()
                janela1.abrirHome().abrir()
            else:
                exibeM()

        def btnCadastro():
            abrindoLogin = CadastraUsuario
            abrindoLogin.abrirCadastro()


                # Cria um frame com borda de tamanho 2 px com raise(efeito de elevação)
                # e com espaço interno horizontal(y) e vertical(x) de 10

        quadro = Frame(janela, bd=2, relief="raised", pady=10, padx=10)
        quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
        fonte = ('Arial', '16', 'bold')  # Define o padrão de fonte

            # Criando os componentes
        lbLogin = Label(quadro, text="Login:", font=fonte, pady=10, padx=10)
        lblMensagem = Label(quadro, text="Usuario não cadastrado", font=fonte, pady=10, padx=10)

        lbSenha = Label(quadro, text="Senha:", font=fonte, pady=10, padx=10)
        edLogin = Entry(quadro, font=fonte)
        edSenha = Entry(quadro, font=fonte, show="*")  # Aparece * no lugar da senha
        #btn para logar user
        btLogar = Button(quadro, font=fonte, text="Logar", fg="green",
            activebackground="#ff8000", activeforeground="white")

        btLogar["command"] = partial(btnLogin)
        btCad = Button(quadro, font=fonte, text="Cadastrar", fg="blue",
                         activebackground="#A9A9A9", activeforeground="lightblue")
        btCad["command"] = partial(btnCadastro)

        # Exibindo os componentes com grig
        lbLogin.grid(row=0, column=0)  # Define que o Label aparecerá na lin 0 col 0
        lbSenha.grid(row=1, column=0)
        edLogin.grid(row=0, column=1)
        edSenha.grid(row=1, column=1)
        btLogar.grid(row=2, column=0)  # Mescla a col 0 + 1 na lin 2
        btCad.grid(row=2, column=1)

        # Configurações da janela

        quadro = Frame(janela, relief="raised", pady=10, padx=10)
        quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
        fonte = ('Arial', '16', 'bold')
        janela.geometry("400x325+200+200")  # Larg x Alt + Left + Top
        janela.title("Login")  # Define o titulo da janela
        janela.mainloop()  # Exibe a janela

janela = LoginView()
janela.MainLogin()