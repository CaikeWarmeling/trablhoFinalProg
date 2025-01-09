from tkinter import *

janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background="#e9edf5")

frameCima = Frame(janela, width=310, height=50, bg="#ff3300", relief='flat')
frameCima.grid(row=0, column=0)

appNome = Label(frameCima, text="Revenda de Veículos", anchor=NW, font=('Ivy 16'), bg="#ff3300", fg="#333333", relief='flat')
appNome.place(x=10, y=20)

frameBaixo = Frame(janela, width=310, height=400, bg="#ffffff", relief='flat')
frameBaixo.grid(row=1, column=0)


janela.mainloop()
