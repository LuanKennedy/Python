from tkinter import *


class Tela1:
    def __init__(self):
        self.janela = Tk()

        self.lb = Label(self.janela, text ="TELA !1")
        self.lb.place(x=100, y=100)

    def exibe(self):
        self.janela.geometry("400+300+200+200")
        self.janela.title("TELA 1")
        self.janela.mainloop()


