# Exemplo 2 - Paineis com abas
from tkinter import *       # importa todas as bibliotecas do tkinter
from tkinter.ttk import *  # Importa todas as bibliotecas ttk para usar o notebook

janela = Tk()
# cria uma variavel abas a atribui o notebook a ela
abas = Notebook(janela, width=490, height=290)  # Atribui o notebook a janela
# Cria um frame para cada aba do notebook
frame_aba1 = Frame(abas)
frame_aba2 = Frame(abas)
frame_aba3 = Frame(abas)
# Cria um Label de exemplo para cada frame
label1 = Label(frame_aba1, text="Esta é a aba1")
label2 = Label(frame_aba2, text="Esta é a aba 2")
label3 = Label(frame_aba3, text="Esta é a aba 3")

# exibe o label no frame com grid
label1.grid()
label2.grid()
label3.grid()
# Adiciona os frames criados nas abas do notebook
abas.add(frame_aba1, text="Aba 1")  # Informa qual frame vai pra aba e o nome da aba
abas.add(frame_aba2, text="Aba 2")
abas.add(frame_aba3, text="Aba 3")
# Exibe o notebook na tela usando pack e configura para redimencionar com a janela
abas.pack(fill=BOTH, expand=1)
# Configurações da janela
janela.geometry("500x300+200+200")  # Largura x Altura + DistaciaEsq + DistandiaTop
janela.title("Abas")  # Define o titulo da janela
janela.mainloop()  # Exibe a janela
