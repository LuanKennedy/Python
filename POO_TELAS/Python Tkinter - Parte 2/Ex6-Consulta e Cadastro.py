# Exemplo 6 - Tela de cadastro e consulta
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


def btBuscar():  # Função do bt buscar(Pesquisar)
    edNome['state'] = "normal"
    edTel['state'] = "normal"
    edEmail['state'] = "normal"
    btSlavar['state'] = "normal"
    edNome.delete(0, END)
    edEmail.delete(0, END)
    edTel.delete(0, END)
    cpf = edCPF.get()
    banco = ConectaBanco()
    where = ("cpf = '%s'" % cpf)
    try:
        reg = banco.select("*", "contatos", where)
    except:
        lbMensagem["text"] = "Erro no BD, notifique o ADM!"
    if not reg:
        lbMensagem["text"] = "Registro não encontrado!"
    else:
        lbMensagem["text"] = "Registro encontrado!"
        for registro in reg:
            edNome.insert(0, registro[1])
            edEmail.insert(0, registro[2])
            edTel.insert(0, registro[3])



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
edCPF = Entry(quadro, font=fonte, width=25)
edNome = Entry(quadro, font=fonte, width=25, state="disabled")
edEmail = Entry(quadro, font=fonte, width=25, state="disabled")
edTel = Entry(quadro, font=fonte, width=25, state="disabled")
btSlavar = Button(quadro, font=fonte, text="Salvar", fg="Blue", state="disabled",
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
btSlavar.grid(row=4, column=0, columnspan=3)

# criando o botão de busca
photoLupa = PhotoImage(file="img/lupa2.png")
logoLupa = photoLupa.subsample(15, 15)
btBusca = Button(quadro, image=logoLupa, bd=0, command=btBuscar)
btBusca.grid(row=0, column=3)

# criando o botão de sair
photoSair = PhotoImage(file="img/sair.png")
logoSair = photoSair.subsample(20, 20)
btExit = Button(janela, image=logoSair, bd=0, command=btExit)
btExit.place(x=495, y=280)

# criando lb mensagem
lbMensagem = Label(janela, text="", font=fonte)
lbMensagem.place(x=20, y=280)

# Configurações da janela
janela.geometry("540x320+200+200")  # Larg x Alt + DistaciaEsq + DistandiaTop
janela.title("Consulta e Cadastro")  # Define o titulo da janela
janela.iconbitmap("img/icone.ico")
janela.mainloop()  # Exibe a janela
