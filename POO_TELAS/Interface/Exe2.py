from tkinter import *

window = Tk() #cria a janela principal

Label(window, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").pack()

#confg da janela
window.geometry("800x600+100+50") #largura x altura + distanciaEsq + distanciaTop
window.title("JOOOJ") #DEFINE O TITULO DA JANELA
window.configure(background="#88DDDD") #defina o fundo
window.mainloop() #exibe a janela