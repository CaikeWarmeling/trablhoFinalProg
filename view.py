from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from classes import *
from main import *

#----------------------------------------Funçôes----------------------------------------#

def changeValueVisualizar(tipo):
    global visualizar
    if tipo in ["motos", "carros"]:
        visualizar = tipo
        for widget in frameDireita.winfo_children():
            widget.destroy()

        viewPreInformations()

    else:
        print("Valor inválido! Use 'motos' ou 'carros'.")

def visualizarInfo():

    treevDados = tree.focus()
    treevDicionario = tree.item(treevDados)
    treeLista = treevDicionario['values']
    valorId = [treeLista[0]]
            
    janelaVisualizar = Tk()
    janelaVisualizar.title("Visualizar informações")
    janelaVisualizar.geometry('2160x70')
    janelaVisualizar.configure(background="#e9edf5")
    janelaVisualizar.resizable(width=False, height=False)

    if visualizar == "carros":
        tabelaHeadCima = ['id','Marca','modelo','ano de fabricação','preço','cor', 'placa', 'número do chassis','número do motor','kilometragem','tipo de combustivel','cilindradas','potência','tipo de transmicao','status','data da venda','numero de portas','airbags','tipo de direcao','tração','espaco no porta malas']

        cabecalioCima = ttk.Treeview(janelaVisualizar, selectmode='extended', columns=tabelaHeadCima, show='headings')
        cabecalioCima.grid(column=0, row=0, sticky='nsew')

        altura = [40, 120, 250, 120, 80, 70, 80, 120, 120, 90, 120, 80, 70, 120, 80, 100, 110, 70, 110, 80, 130]

        n = 0
        for col in tabelaHeadCima:
            cabecalioCima.heading(col, text=col.title(), anchor=CENTER)
            cabecalioCima.column(col, width=altura[n], anchor="nw")
            n += 1

        View = viewInfoCarros(valorId)

        for item in View:
            cabecalioCima.insert('', 'end', values=item)

    elif visualizar == "motos":
        tabelaHeadCima = ['id','Marca','modelo','ano de fabricação','preço','cor', 'placa', 'número do chassis','número do motor','kilometragem','tipo de combustivel','cilindradas','potência','tipo de transmicao','status','data da venda','tipo da moto', 'peso', 'tipo de freio', 'acessorios especiais']

        cabecalioCima = ttk.Treeview(janelaVisualizar, selectmode='extended', columns=tabelaHeadCima, show='headings')
        cabecalioCima.grid(column=0, row=0, sticky='nsew')

        altura = [40, 120, 250, 120, 80, 70, 80, 120, 120, 90, 120, 80, 70, 120, 80, 100, 110, 70, 110, 210]

        n = 0
        for col in tabelaHeadCima:
            cabecalioCima.heading(col, text=col.title(), anchor=CENTER)
            cabecalioCima.column(col, width=altura[n], anchor="nw")
            n += 1

        View = viewInfoMotos(valorId)

        for item in View:
            cabecalioCima.insert('', 'end', values=item)
    else:
        print("Erro!")

def deletarInfo():
    try:
        treevDados = tree.focus()
        treevDicionario = tree.item(treevDados)
        treeLista = treevDicionario['values']
        valorId = [treeLista[0]]

        if visualizar == "carros":
            deleteInfoCarros(valorId)
            messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')

        elif visualizar == "motos":
            deleteInfoMotos(valorId)
            messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')

        for widget in frameDireita.winfo_children():
            widget.destroy()

        viewPreInformations()

    except IndentationError:
        messagebox.showerror('Erro','Selecione um dos dados na tabela')

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

#----------------------------------------Botões----------------------------------------#

visualizar = "carros"

botaoCarro = Button(frameBaixo, command=lambda:changeValueVisualizar("carros"), text='Carros', width=10, anchor=NW, font=('ivy 14 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoCarro.place(x=15, y=60)

botaomoto = Button(frameBaixo, text='motos', command=lambda:changeValueVisualizar("motos"), width=10, anchor=NW, font=('ivy 14 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaomoto.place(x=160, y=60)

botaoVisualizar = Button(frameBaixo, command=visualizarInfo, text='Visualizar', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoVisualizar.place(x=15, y=460)

botaoInserir = Button(frameBaixo, text='Incerir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoInserir.place(x=15, y=500)

botaoEditar = Button(frameBaixo, text='Editar', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoEditar.place(x=15, y=540)

botaoExcluir = Button(frameBaixo, text='Excluir', command=deletarInfo, width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoExcluir.place(x=15, y=580)

#----------------------------------------Frame da direita----------------------------------------#

frameDireita = Frame(janela, width=970, height=720, bg="#e9edf5", relief="flat")
frameDireita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

def viewPreInformations():

    global tree

    tabelaHead = ['id','Marca','modelo','ano de fabricação','cor','placa', 'preço']

    tree = ttk.Treeview(frameDireita, selectmode='extended', columns=tabelaHead, show='headings')

    barraScroll = ttk.Scrollbar(frameDireita, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=barraScroll.set)

    tree.grid(column=0, row=0, sticky='nsew')
    barraScroll.grid(column=1, row=0, sticky='ns')
    frameDireita.grid_rowconfigure(0, weight=12)

    posicaoHead = ["nw","nw", "nw", "nw", "nw", "center", "center"]
    altura = [40, 150, 250, 150, 100, 150, 130]

    n = 0
    for col in tabelaHead:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=altura[n], anchor=posicaoHead[n])
        n+=1

    if visualizar == "carros":
        preView = preViewInfoCarros()

    elif visualizar == "motos":
        preView = preViewInfoMotos()

    for item in preView:
        tree.insert('', 'end', values=item)
    
viewPreInformations()

#----------------------------------------Rodando----------------------------------------#

janela.mainloop()