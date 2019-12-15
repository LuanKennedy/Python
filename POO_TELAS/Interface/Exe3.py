from tkinter import *

window = Tk() #cria a janela principal

lb = Label(window, text="salve mundo")
lb.place(x=100, y=100)

#confg da janela
window.geometry("800x600+100+50") #largura x altura + distanciaEsq + distanciaTop
window.title("JOOOJ") #DEFINE O TITULO DA JANELA
window.configure(background="#88DDDD") #defina o fundo
window.mainloop() #exibe a janela