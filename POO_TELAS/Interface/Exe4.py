from tkinter import *

def bt_click():
    print("clik")
    lb["text"] = "FUNCIONOU"


window = Tk() #cria a janela principal

bt = Button(window, width=20, text="OK", command=bt_click)

bt.place(x=100, y=100)

lb = Label(window, text="teste")

lb.place(x=100, y=150)


#confg da janela
window.geometry("800x600+100+50") #largura x altura + distanciaEsq + distanciaTop
window.title("JOOOJ") #DEFINE O TITULO DA JANELA
window.configure(background="#FF8000") #defina o fundo
window.mainloop() #exibe a janela