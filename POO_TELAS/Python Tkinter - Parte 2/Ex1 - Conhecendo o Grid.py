# Exemplo 1 - Conhecendo o Grid
from tkinter import *

janela = Tk()  # Cria a tela principal
# Criando os componentes
lb1 = Label(janela, text="Label 1", bg="green")
# Atribui um label a lb1
lb2 = Label(janela, text="Label 2", bg="pink")
lb3 = Label(janela, text="Label 3", bg="blue")
lb4 = Label(janela, text="Label 4", bg="red")
# Exibindo os componentes com grig
lb1.grid(row=3, column=5)
# Define que o Label aparecerá na linha 3 coluna 5
lb2.grid(row=3, column=7)
lb3.grid(row=300, column=300)
lb4.grid(row=1000, column=5000)
'''OBS: Independente do valor digitado na linha ou coluna, 
os componetes ocuparão a linha vazia mais proxima do topo 
e coluna vazia mais proxima da esquerda'''
# Configurações da janela
janela.geometry("500x200+200+200")  # Larg x Alt + left + Top
janela.title("Conhecendo o Grid")  # Define titulo da janela
janela.mainloop()  # Exibe a janela
