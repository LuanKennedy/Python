from tkinter import *
from functools import partial
from tela1 import Tela1
from tela2 import Tela2


def bt_click(botao):
    op = (botao["text"])
    if op == "Tela 1":
        #janela.destroy()
        tela = Tela1()
        tela.exibe()

    elif op == "Tela 2":
        tela = Tela2()
        tela.exibe()




janela = Tk()

bt1 = Button(janela, width=15, text="Tela 1")
bt1["command"] = partial(bt_click, bt1)

bt2 = Button(janela, width=15, text="Tela 2")
bt2["command"] = partial(bt_click, bt2)

bt1.place(x=30, y=10)
bt2.place(x=150, y=10)

janela.geometry("540x320+200+200")
janela.title("Menu")
janela.mainloop()