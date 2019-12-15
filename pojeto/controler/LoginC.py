from pojeto.banco.logar import Login
from tkinter import *

class LoginC:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def verificar(self):
        loginM = Login(self.login, self.senha)
        verificou = loginM.autenticar()
        if (verificou):
            return True
        else:
            return print("USER NÃO CADASTRADO")

    def abrir(self):
        janela = Tk()  # Cria a tela principal
        janela.resizable(0, 0)  # Impede que a telaseja redimensionada
        quadro = Frame(janela, bd=2, relief="raised", pady=10, padx=10)
        quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
        fonte = ('Arial', '16', 'bold')

