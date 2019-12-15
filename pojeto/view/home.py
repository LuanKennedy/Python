from tkinter import *       # importa todas as bibliotecas do tkinter
from pojeto.view.admProdutos import Adm
from pojeto.view.venda import Vendas
from pojeto.view.listagem import Listagem
from pojeto.view.listagemVendas import ListagemVendas
from functools import partial


class Home:
    def abrirHome(self):
        janela = Tk()  # Cria a tela principal
        janela.resizable(0, 0)
        quadro = Frame(janela, relief="raised", pady=10, padx=10)
        quadro.place(x=20, y=20)  # posiciona o quadro na posição xy
        fonte = ('Arial', '16', 'bold')

        def btnProdutos():
            janela.destroy()
            abrindoProdutos = Adm()
            abrindoProdutos.principal()
            print('passou aqui')

        def btnVendas():
            janela.destroy()
            abrindoVendas = Vendas()
            abrindoVendas.abrirVendas()

        def btnListagemP():
            abrindoListagem = Listagem()
            janela.destroy()
            abrindoListagem.abrirListagem()

        def btnListagemV():
            abrindoListagemV = ListagemVendas()
            janela.destroy()
            abrindoListagemV.abrirlistagemVendas()




            #CRIANDO A CACETA DOS BOTAO


        btnListar = Button(quadro, font=fonte, text="Listagem dos produtos", fg="#ff8000",
        activebackground="#A9A9A9", activeforeground="white")
        btnListar["command"] = partial(btnListagemP)
        btnAdm = Button(quadro, font=fonte, text="Administração dos produtos", fg="#ff8000",
        activebackground="#A9A9A9", activeforeground="white")
        btnAdm["command"] = partial(btnProdutos)
        btnVender = Button(quadro, font=fonte, text=" Vender produtos", fg="#ff8000",
        activebackground="#A9A9A9", activeforeground="white")
        btnVender["command"] = partial(btnVendas)
        btnRegistro = Button(quadro, font=fonte, text="Registro de Vendas", fg="#ff8000",
        activebackground="#A9A9A9", activeforeground="white")
        btnRegistro["command"] = partial(btnListagemV)
        btnEspaco = Button(quadro, bd=0) #espaçamento entre os botões heheh
        btnEspaco2 = Button(quadro, bd=0)
        btnEspaco3 = Button(quadro, bd=0)

        #EXIBINDO ESSE CARAI

        btnListar.grid(row=1, column=2)
        btnEspaco.grid(row=2, column=2)
        btnAdm.grid(row=3, column=2)
        btnEspaco2.grid(row=4, column=2)
        btnVender.grid(row=5, column=2)
        btnEspaco3.grid(row=6, column=2)
        btnRegistro.grid(row=7, column=2)





        janela.geometry("390x320+200+200")  # Larg x Alt + DistaciaEsq + DistandiaTop
        janela.title("HOME")  # Define o titulo da janela
        #janela.iconbitmap("img/icone.ico")
        janela.mainloop()  # Exibe a janela




