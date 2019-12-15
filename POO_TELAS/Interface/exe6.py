from tkinter import *

def bt_click():
    print(ed.get())
    lb["text"] =ed.get()


window = Tk() #cria a janela principal

ed = Entry(window, width=20)
ed.place(x=100, y=100) #entry é o campo de texto

bt = Button(window, width=16, text="Botao 1 ", command=bt_click)
bt.place(x=100, y=150)

lb= Label(window, text="DIGITA POHAH")
lb.place(x=100, y=170)

#confg da janela
window.geometry("800x600+100+50") #largura x altura + distanciaEsq + distanciaTop
window.title("JOOOJ") #DEFINE O TITULO DA JANELA
window.configure(background="#FF8000") #defina o fundo
window.mainloop() #exibe a janela
