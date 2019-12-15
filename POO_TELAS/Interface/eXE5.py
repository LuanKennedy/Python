from tkinter import *
from functools import partial

def bt_click(botao):
    print(botao["text"])
    lb["text"] = "clicou n "+botao["text"]+"jooj"


window = Tk() #cria a janela principal

bt1 = Button(window, width=20, text="botao 1")

bt1["command"] = partial(bt_click, bt1)

bt1.place(x=100, y=100)

bt2 = Button(window, width=20,  text="botao 2")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=150)

lb = Label(window, text="teste")
lb.place(x=100, y=170)

#confg da janela
window.geometry("800x600+100+50") #largura x altura + distanciaEsq + distanciaTop
window.title("JOOOJ") #DEFINE O TITULO DA JANELA
window.configure(background="#FF8000") #defina o fundo
window.mainloop() #exibe a janela