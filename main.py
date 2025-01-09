from tkinter import *
from tkinter import ttk

#----------------------------------------Site----------------------------------------#

janela = Tk()
janela.title("")
janela.geometry('1280x720')
janela.configure(background="#e9edf5")
janela.resizable(width=False, height=False)

#----------------------------------------Frame de cima----------------------------------------#

frameCima = Frame(janela, width=310, height=50, bg="#ff3300", relief='flat')
frameCima.grid(row=0, column=0)

appNome = Label(frameCima, text="Revenda de Veículos", anchor=NW, font=('Ivy 18 bold'), bg="#ff3300", fg="#333333", relief='flat')
appNome.place(x=10, y=15)

#----------------------------------------Frame de Baixo----------------------------------------#

frameBaixo = Frame(janela, width=310, height=670, bg="#ffffff", relief="flat")
frameBaixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

escolherVisualizar = Label(frameBaixo, text="Visualizar tabela:", anchor=NW, font=('Ivy 16 bold'), bg="#ffffff", fg="#333333", relief='flat')
escolherVisualizar.place(x=10, y=25)

botaoCarro = Button(frameBaixo, text='Carros', width=10, anchor=NW, font=('ivy 14 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoCarro.place(x=15, y=60)

botaomoto = Button(frameBaixo, text='motos', width=10, anchor=NW, font=('ivy 14 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaomoto.place(x=160, y=60)

botaoInserir = Button(frameBaixo, text='Incerir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoInserir.place(x=15, y=500)

botaoEditar = Button(frameBaixo, text='Editar', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoEditar.place(x=15, y=540)

botaoExcluir = Button(frameBaixo, text='Excluir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoExcluir.place(x=15, y=580)

#----------------------------------------Frame da direita----------------------------------------#

frameDireita = Frame(janela, width=970, height=720, bg="#e9edf5", relief="flat")
frameDireita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

tabelaHead = ['Marca','modelo','ano de fabricação','cor','placa', 'view']

tree = ttk.Treeview(frameDireita, selectmode='extended', columns=tabelaHead, show='headings')

barraScroll = ttk.Scrollbar(frameDireita, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=barraScroll.set)

tree.grid(column=0, row=0, sticky='nsew')
barraScroll.grid(column=1, row=0, sticky='ns')
frameDireita.grid_rowconfigure(0, weight=12)

lista = ["nw", "nw", "nw", "nw", "center", "center"]
altura = [150, 300, 150, 120, 150, 100]
n = 0

for col in tabelaHead:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=altura[n], anchor=lista[n])
    n+=1

tabelaNomes = [["fiat", "Strada fire 1.4 CS", "2005/2005", "preta", "mph4400"],
               ["mitsubishi", "l200 triton HPE", "2009/2009", "azul", "mon6751"],
               ["mitsubishi", "lancer HLE", "2016/2016", "prata", "sla1234"]
               ]

for item in tabelaNomes:
    tree.insert('', 'end', values=item)

janela.mainloop()
