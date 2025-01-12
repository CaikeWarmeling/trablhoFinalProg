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

def renderinput(frame, text, x, y):
    label = Label(frame, text=text, anchor=NW, font=('Ivy, 10 bold'), bg="#333333", fg="#ffffff", relief='flat')
    label.place(x = x, y= y)
    entry = Entry(frame, width=45, justify='left', relief='solid')
    entry.place(x = x, y = y+30)

    return entry

def view():

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

        View = viewCarro(valorId)

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

        View = viewMoto(valorId)

        for item in View:
            cabecalioCima.insert('', 'end', values=item)
    else:
        print("Erro!")

def insert():

    janelaInserir = Tk()
    janelaInserir.title("Inserir veiculo")
    janelaInserir.geometry('640x720')
    janelaInserir.configure(background="#e9edf5")
    janelaInserir.resizable(width=False, height=False)

    marca = renderinput(janelaInserir,"marca do veiculo:", 10, 10)
    modelo = renderinput(janelaInserir,"modelo do veiculo:", 350, 10)
    ano = renderinput(janelaInserir,"ano de fabircação do veiculo:", 10, 70)
    preco = renderinput(janelaInserir,"preço do veiculo:", 350, 70)
    cor = renderinput(janelaInserir,"cor do veiculo:", 10, 130)
    placa = renderinput(janelaInserir,"placa do veiculo", 350, 130)
    chassis = renderinput(janelaInserir,"número do chassis do veiculo:", 10, 190)
    numMotor = renderinput(janelaInserir,"número do motor do veiculo:", 350, 190)
    kilometragem = renderinput(janelaInserir,"kilometragem do veiculo:", 10, 250)
    tipoCombustivel = renderinput(janelaInserir,"tipo de combustivel do veiculo:", 350, 250)
    cilindradas = renderinput(janelaInserir,"cilindradas do veiculo:", 10, 310)
    potencia = renderinput(janelaInserir,"potência do veiculo:", 350, 310)
    transmissao = renderinput(janelaInserir,"tipo de transmissão do veiculo:", 10, 370)
    status = renderinput(janelaInserir,"status do veiculo:", 350, 370)

    if visualizar == "carros":
        numeroPortas = renderinput(janelaInserir,"numero de Portas do carro:", 10, 430)
        airbags = renderinput(janelaInserir,"airbags do carro:", 350, 430)
        tipoDirecao = renderinput(janelaInserir,"tipoDireção do carro:", 10, 490)
        tracao = renderinput(janelaInserir,"tipo de tração do carro:", 350, 490)
        espacoPortaMalas = renderinput(janelaInserir,"espaço do porta malas do carro:", 10, 550)

        botaoInserir = Button(janelaInserir, command=lambda:insertInClassCarroAndPutInDB(marca.get(),modelo.get(),ano.get(),preco.get(),cor.get(),placa.get(),chassis.get(),numMotor.get(),kilometragem.get(),tipoCombustivel.get(),cilindradas.get(),potencia.get(),transmissao.get(),status.get(),numeroPortas.get(),airbags.get(),tipoDirecao.get(),tracao.get(),espacoPortaMalas.get()), text='Incerir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
        botaoInserir.place(x=350, y=565)

    elif visualizar == "motos":
        tipoMoto = renderinput(janelaInserir,"tipo de moto:", 10, 430)
        peso = renderinput(janelaInserir,"peso da moto:", 350, 430)
        tipoFreio = renderinput(janelaInserir,"tipo de freio da mato:", 10, 490)
        acessoriosEspeciais = renderinput(janelaInserir,"acessorios especiais:", 350, 490)

        botaoInserir = Button(janelaInserir, command=lambda:insertInClassMotoAndPutInDB(marca.get(),modelo.get(),ano.get(),preco.get(),cor.get(),placa.get(),chassis.get(),numMotor.get(),kilometragem.get(),tipoCombustivel.get(),cilindradas.get(),potencia.get(),transmissao.get(),status.get(),tipoMoto.get(),peso.get(),tipoFreio.get(),acessoriosEspeciais.get()), text='Incerir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
        botaoInserir.place(x=350, y=565)

    def insertInClassCarroAndPutInDB(marca,modelo,anoFabricacao,preco,cor,placa,chassis,numeroMotor,kilometragem,tipoCombustivel,cilindradas,potencia,tipoTransmicao,status,numeroPortas,airbags,tipoDirecao,tracao,espacoPortaMalas):

        carro = Carro(marca,modelo,anoFabricacao,preco,cor,placa,chassis,numeroMotor,kilometragem,tipoCombustivel,cilindradas,potencia,tipoTransmicao,status,numeroPortas,airbags,tipoDirecao,tracao,espacoPortaMalas)
        carro.insertCarro()
        messagebox.showinfo('Sucesso','Os dados foram adicionados com sucesso!')
        for widget in frameDireita.winfo_children():
            widget.destroy()

        viewPreInformations()
        janelaInserir.destroy()

    def insertInClassMotoAndPutInDB(marca,modelo,anoFabricacao,preco,cor,placa,chassis,numeroMotor,kilometragem,tipoCombustivel,cilindradas,potencia,tipoTransmicao,status,tipoMoto,peso,tipoFreio,acessoriosEspeciais):

        moto = Moto(marca,modelo,anoFabricacao,preco,cor,placa,chassis,numeroMotor,kilometragem,tipoCombustivel,cilindradas,potencia,tipoTransmicao,status,tipoMoto,peso,tipoFreio,acessoriosEspeciais)
        moto.insertMoto()
        messagebox.showinfo('Sucesso','Os dados foram adicionados com sucesso!')
        for widget in frameDireita.winfo_children():
            widget.destroy()

        viewPreInformations()
        janelaInserir.destroy()

    janelaInserir.mainloop()

def update():

    treevDados = tree.focus()
    treevDicionario = tree.item(treevDados)
    treeLista = treevDicionario['values']
    valorId = treeLista[0]

    janelaEditar = Tk()
    janelaEditar.title("Editar veiculo")
    janelaEditar.geometry('640x200')
    janelaEditar.configure(background="#e9edf5")
    janelaEditar.resizable(width=False, height=False)

    preco = renderinput(janelaEditar,"Preço",10,10)
    kilometragem = renderinput(janelaEditar,"kilometragem",350,10)
    status = renderinput(janelaEditar,"status",10,70)
    dataVenda = renderinput(janelaEditar,"data da venda",350,70)

    def insertValuesInEditar(preco, kilometragem,status,dataVenda, valorId):
        lista = []
        lista.append(preco)
        lista.append(kilometragem)
        lista.append(status)
        lista.append(dataVenda)
        lista.append(valorId)

        if visualizar == "carros":
            editCarro(lista)
            for widget in frameDireita.winfo_children():
                widget.destroy()

            viewPreInformations()
            messagebox.showinfo('Sucesso','Os dados foram editados com sucesso')
            janelaEditar.destroy()

        elif visualizar == "motos":
            editMoto(lista)
            for widget in frameDireita.winfo_children():
                widget.destroy()

            viewPreInformations()
            messagebox.showinfo('Sucesso','Os dados foram editados com sucesso')
            janelaEditar.destroy()

    botaoEditar = Button(janelaEditar, command=lambda:insertValuesInEditar(preco.get(),kilometragem.get(),status.get(),dataVenda.get(),valorId), text='Editar', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
    botaoEditar.place(x=260, y=150)

    janelaEditar.mainloop

def delete():
    try:
        treevDados = tree.focus()
        treevDicionario = tree.item(treevDados)
        treeLista = treevDicionario['values']
        valorId = [treeLista[0]]

        if visualizar == "carros":
            deleteCarro(valorId)
            messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')

        elif visualizar == "motos":
            deleteMoto(valorId)
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

botaoVisualizar = Button(frameBaixo, command=view, text='Visualizar', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoVisualizar.place(x=15, y=460)

botaoInserir = Button(frameBaixo, command=insert, text='Incerir', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoInserir.place(x=15, y=500)

botaoEditar = Button(frameBaixo, command=update, text='Editar', width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
botaoEditar.place(x=15, y=540)

botaoExcluir = Button(frameBaixo, text='Excluir', command=delete, width=10, anchor=NW, font=('ivy 12 bold'), bg="#aaaaaa", fg="#333333", relief='raised', overrelief='ridge')
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
        preView = preViewCarros()

    elif visualizar == "motos":
        preView = preViewMotos()

    for item in preView:
        tree.insert('', 'end', values=item)
    
viewPreInformations()

#----------------------------------------Rodando----------------------------------------#

janela.mainloop()