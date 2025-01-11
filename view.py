from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from classes import *
from main import *


#----------------------------------------Funçôes----------------------------------------#
global tree

def obter_atributos_como_lista(self):
    # Retorna uma lista de listas com os valores dos atributos
    return [[self.marca], [self.modelo], [self.anoDeFabricacao], [self.preco], [self.cor], [self.placa], [self.numeroChassis], [self.numeroMotor], [self.kilometragem], [self.tipoCombustivel], [self.cilindradas], [self.potencia], [self.tipoTransmicao], [self.status], [self.numeroPortas], [self.airbags], [self.tipoDirecao], [self.tracao], [self.espacoPortaMalas]]

def incertInClassCarroAndPutInDB(marca, modelo, ano, preco, cor, placa, chassis, numMotor, kilometragem, tipoCombustivel, cilindradas, potencia, transmissao, status, numeroPortas, airbags, tipoDirecao, tracao, espacoPortaMalas):
    marca = marca.get()
    modelo = modelo.get()
    ano = ano.get()
    preco = preco.get()
    cor= cor.get()
    placa = placa.get()
    chassis = chassis.get()
    numMotor = numMotor.get()
    kilometragem = kilometragem.get()
    tipoCombustivel = tipoCombustivel.get()
    cilindradas = cilindradas.get()
    potencia = potencia.get()
    transmissao = transmissao.get()
    status = status.get()
    numeroPortas = numeroPortas.get()
    airbags = airbags.get()
    tipoDirecao = tipoDirecao.get()
    tracao = tracao.get()
    espacoPortaMalas = espacoPortaMalas.get()

    objeto = Carro(marca, modelo, ano, preco, cor, placa, chassis, numMotor, kilometragem, tipoCombustivel, cilindradas, potencia, transmissao, status, numeroPortas, airbags, tipoDirecao, tracao, espacoPortaMalas)
    atributos = objeto.obter_atributos_como_lista()

    incertInfoCarros(atributos)

def insertCarros():
    janelaInserir = Tk()
    janelaInserir.title("Inserir carro")
    janelaInserir.geometry('640x720')
    janelaInserir.configure(background="#e9edf5")
    janelaInserir.resizable(width=False, height=False)
    
    l_marca = Label(janelaInserir, text='marca do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_marca.place(x=10, y=10)
    e_marca = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_marca.place(x=10, y=40)

    l_modelo = Label(janelaInserir, text='modelo do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_modelo.place(x=350, y=10)
    e_modelo = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_modelo.place(x=350, y=40)

    l_ano = Label(janelaInserir, text='ano de fabircação do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_ano.place(x=10, y=70)
    e_ano = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_ano.place(x=10, y=100)

    l_preco = Label(janelaInserir, text='preço do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_preco.place(x=350, y=70)
    e_preco = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_preco.place(x=350, y=100)

    l_cor = Label(janelaInserir, text='cor do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_cor.place(x=10, y=130)
    e_cor = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_cor.place(x=10, y=160)

    l_placa = Label(janelaInserir, text='placa do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_placa.place(x=350, y=130)
    e_placa = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_placa.place(x=350, y=160)

    l_chassis = Label(janelaInserir, text='número do chassis do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_chassis.place(x=10, y=190)
    e_chassis = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_chassis.place(x=10, y=220)

    l_numMotor = Label(janelaInserir, text='número do motor do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_numMotor.place(x=350, y=190)
    e_numMotor = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_numMotor.place(x=350, y=220)
    
    l_kilometragem = Label(janelaInserir, text='kilometragem do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_kilometragem.place(x=10, y=250)
    e_kilometragem = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_kilometragem.place(x=10, y=280)

    l_tipoCombustivel = Label(janelaInserir, text='tipo de combustivel do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_tipoCombustivel.place(x=350, y=250)
    e_tipoCombustivel = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_tipoCombustivel.place(x=350, y=280)

    l_cilindradas = Label(janelaInserir, text='cilindradas do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_cilindradas.place(x=10, y=310)
    e_cilindradas = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_cilindradas.place(x=10, y=340)

    l_potencia = Label(janelaInserir, text='potência do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_potencia.place(x=350, y=310)
    e_potencia = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_potencia.place(x=350, y=340)

    l_transmissao = Label(janelaInserir, text='tipo de transmissão do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_transmissao.place(x=10, y=370)
    e_transmissao = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_transmissao.place(x=10, y=400)

    l_status = Label(janelaInserir, text='status do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_status.place(x=350, y=370)
    e_status = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_status.place(x=350, y=400)

    l_numeroPortas = Label(janelaInserir, text='numero de Portas do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_numeroPortas.place(x=10, y=430)
    e_numeroPortas = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_numeroPortas.place(x=10, y=460)

    l_airbags = Label(janelaInserir, text='airbags do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_airbags.place(x=350, y=430)
    e_airbags = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_airbags.place(x=350, y=460)

    l_tipoDirecao = Label(janelaInserir, text='tipoDireção do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_tipoDirecao.place(x=10, y=490)
    e_tipoDirecao = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_tipoDirecao.place(x=10, y=520)

    l_tracao = Label(janelaInserir, text='tipo de tração do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_tracao.place(x=350, y=490)
    e_tracao = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_tracao.place(x=350, y=520)

    l_espacoPortaMalas = Label(janelaInserir, text='espaço do porta malas do carro:', anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    l_espacoPortaMalas.place(x=10, y=550)
    e_espacoPortaMalas = Entry(janelaInserir, width=45, justify='left', relief='solid')
    e_espacoPortaMalas.place(x=10, y=580)

    botaoInserir = Button(janelaInserir, command=lambda: incertInClassCarroAndPutInDB(e_marca, e_modelo, e_ano, e_preco, e_cor, e_placa, e_chassis, e_numMotor, e_kilometragem, e_tipoCombustivel, e_cilindradas, e_potencia, e_transmissao, e_status, e_numeroPortas, e_airbags, e_tipoDirecao, e_tracao, e_espacoPortaMalas), text='Incerir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
    botaoInserir.place(x=350, y=565)

    janelaInserir.mainloop()

def visualizarCarros():

    treevDados = tree.focus()
    treevDicionario = tree.item(treevDados)
    treeLista = treevDicionario['values']
    valorId = [treeLista[0]]
            
    janelaVisualizar = Tk()
    janelaVisualizar.title("Visualizar informações do carro")
    janelaVisualizar.geometry('2160x70')
    janelaVisualizar.configure(background="#e9edf5")
    janelaVisualizar.resizable(width=False, height=False)

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

def deletarCarros():
    try:
        treevDados = tree.focus()
        treevDicionario = tree.item(treevDados)
        treeLista = treevDicionario['values']
        valorId = [treeLista[0]]

        deleteInfoCarros(valorId)
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

botaoCarro = Button(frameBaixo, text='Carros', width=10, anchor=NW, font=('ivy 14 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoCarro.place(x=15, y=60)

botaomoto = Button(frameBaixo, text='motos', width=10, anchor=NW, font=('ivy 14 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaomoto.place(x=160, y=60)

botaoVisualizar = Button(frameBaixo,command=visualizarCarros, text='Visualizar', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoVisualizar.place(x=15, y=460)

botaoInserir = Button(frameBaixo, command=insertCarros, text='Incerir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoInserir.place(x=15, y=500)

botaoEditar = Button(frameBaixo, text='Editar', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoEditar.place(x=15, y=540)

botaoExcluir = Button(frameBaixo, command=deletarCarros, text='Excluir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
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

    preView = preViewInfoCarros()

    for item in preView:
        tree.insert('', 'end', values=item)

viewPreInformations()

janela.mainloop()
