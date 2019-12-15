# Exemplo 5 - Tela de cadastro
from tkinter import *
from conectabanco import ConectaBanco


def btExit():  # Função para fechar a janela
    janela.destroy()


def btSlavar():  # Função do bt confirma(Cadastrar)
    cpf = edCPF.get()
    nome = edNome.get()
    email = edEmail.get()
    tel = edTel.get()
    banco = ConectaBanco()
    valores = ("'%s','%s','%s','%s'" % (cpf, nome, email, tel))
    try:
        banco.insert("contatos", valores)
    except:
        lbMensagem["text"] = "Não foi possivel cadastrar!"
    else:
        lbMensagem["text"] = "Cadastrado com sucesso!"


janela = Tk()  # Cria a tela principal
janela.resizable(0, 0)
quadro = Frame(janela, bd=2, relief="raised", pady=10, padx=10)
quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
fonte = ('Arial', '16', 'bold')  # Define o padrão de fonte

# Criando os componentesdo formulario
lbCPF = Label(quadro, text="CPF:", font=fonte, pady=10, padx=10)
lbNome = Label(quadro, text="Nome:", font=fonte, pady=10, padx=10)
lbEmail = Label(quadro, text="E-mail:", font=fonte, pady=10, padx=10)
lbTel = Label(quadro, text="Telefone:", font=fonte, pady=10, padx=10)
edCPF = Entry(quadro, font=fonte, width=15)
edNome = Entry(quadro, font=fonte, width=15)
edEmail = Entry(quadro, font=fonte, width=15)
edTel = Entry(quadro, font=fonte, width=15)
btSlavar = Button(quadro, font=fonte, text="Salvar", fg="Blue",
activebackground="#A9A9A9", activeforeground="white", command=btSlavar)

# Exibindo os componentes do formulario com grid
lbCPF.grid(row=0, column=0)
lbNome.grid(row=1, column=0)
lbEmail.grid(row=2, column=0)
lbTel.grid(row=3, column=0)
edCPF.grid(row=0, column=1)
edNome.grid(row=1, column=1)
edEmail.grid(row=2, column=1)
edTel.grid(row=3, column=1)
btSlavar.grid(row=4, column=0, columnspan=2)

# criando o botão de sair
photo = PhotoImage(file="img/sair.png")
logo = photo.subsample(20, 20)
btExit = Button(janela, image=logo, bd=0, command=btExit)
btExit.place(x=320, y=280)

# criando lb mensagem
lbMensagem = Label(janela, text="", font=fonte)
lbMensagem.place(x=20, y=280)

# Configurações da janela
janela.geometry("370x320+200+200")  # Larg x Alt + DistaciaEsq + DistandiaTop
janela.title("Cadastro")  # Define o titulo da janela
janela.iconbitmap("img/icone.ico")
janela.mainloop()  # Exibe a janela
