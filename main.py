import sqlite3 as lite

conexao = lite.connect('veiculos.db')

#----------------------------------------Carros----------------------------------------#

#FILTRAR carros
def filterCarros(marca, modelo, ano, placa):
    listFilter = []
    with conexao:
        cur = conexao.cursor()
        querry = '''SELECT id, marca, modelo, anoFabricacao, cor, placa, kilometragem, status, preco 
                    FROM carros 
                    WHERE (? is NULL or marca=? or modelo=? or anoFabricacao=? or placa=?)'''
        cur.execute(querry, [marca, marca, modelo, ano, placa])
        informacoes = cur.fetchall()
        for i in informacoes:
            listFilter.append(i)
    return listFilter

#VISUALIZAR carro
def viewCarro(id):
    view = []
    with conexao:
        cur = conexao.cursor()
        querry = "SELECT * FROM carros WHERE id=?"
        cur.execute(querry, id)
        informacoes = cur.fetchall()
        for i in informacoes:
            view.append(i)
    return view

#PRE VISUALIZAR carros
def preViewCarros():
    preView = []
    with conexao:
        cur = conexao.cursor()
        querry = "SELECT id, marca, modelo, anoFabricacao, cor, placa, kilometragem, status, preco FROM carros"
        cur.execute(querry)
        preVisualizar = cur.fetchall()
        for i in preVisualizar:
            preView.append(i)
    return preView

#EDITAR carro
def editCarro(i):
    #i = ['preco','kilometragem','status','dataVenda',id]
    with conexao:
        cur = conexao.cursor()
        querry = "UPDATE carros SET preco=?, kilometragem=?, status=?, dataVenda=? WHERE id=?"
        cur.execute(querry, i)

#DELETAR carro
def deleteCarro(id):
    with conexao:
        cur = conexao.cursor()
        querry = "DELETE FROM carros WHERE id=?"
        cur.execute(querry, id)

#----------------------------------------Motos----------------------------------------#

#FILTRAR motos
def filterMotos(marca, modelo, ano, placa):
    listFilter = []
    with conexao:
        cur = conexao.cursor()
        querry = '''SELECT id, marca, modelo, anoFabricacao, cor, placa, kilometragem, status, preco 
                    FROM motos 
                    WHERE (? is NULL or marca=? or modelo=? or anoFabricacao=? or placa=?)'''
        cur.execute(querry, [marca, marca, modelo, ano, placa])
        informacoes = cur.fetchall()
        for i in informacoes:
            listFilter.append(i)
    return listFilter

#VISUALIZAR moto
def viewMoto(id):
    view = []
    with conexao:
        cur = conexao.cursor()
        querry = "SELECT * FROM motos WHERE id=?"
        cur.execute(querry, id)
        informacoes = cur.fetchall()
        for i in informacoes:
            view.append(i)
    return view

#PRE VISUALIZAR motos
def preViewMotos():
    preView = []
    with conexao:
        cur = conexao.cursor()
        querry = "SELECT id, marca, modelo, anoFabricacao, cor, placa, kilometragem, status, preco FROM motos"
        cur.execute(querry)
        preVisualizar = cur.fetchall()
        for i in preVisualizar:
            preView.append(i)
    return preView

#EDITAR moto
def editMoto(i):
    #i = ['preco','kilometragem','status','dataVenda',id]
    with conexao:
        cur = conexao.cursor()
        querry = "UPDATE motos SET preco=?, kilometragem=?, status=?, dataVenda=? WHERE id=?"
        cur.execute(querry, i)

#DELETAR moto
def deleteMoto(id):
    with conexao:
        cur = conexao.cursor()
        querry = "DELETE FROM motos WHERE id=?"
        cur.execute(querry, id)