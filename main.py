import sqlite3 as lite

conexao = lite.connect('veiculos.db')

#----------------------------------------Carros----------------------------------------#

#VISUALIZAR carros
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
        querry = "SELECT id, marca, modelo, anoFabricacao, cor, placa, preco FROM carros"
        cur.execute(querry)
        preVisualizar = cur.fetchall()
        for i in preVisualizar:
            preView.append(i)
    return preView

#EDITAR carros
def editCarro(i):
    with conexao:
        cur = conexao.cursor()
        querry = "UPDATE carros SET preco=?, kilometragem=?, status=?, dataVenda=? WHERE id=?"
        cur.execute(querry, i)

#DELETAR carros
def deleteCarro(id):
    with conexao:
        cur = conexao.cursor()
        querry = "DELETE FROM carros WHERE id=?"
        cur.execute(querry, id)

#----------------------------------------Motos----------------------------------------#

#VISUALIZAR motos
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
        querry = "SELECT id, marca, modelo, anoFabricacao, cor, placa, preco FROM motos"
        cur.execute(querry)
        preVisualizar = cur.fetchall()
        for i in preVisualizar:
            preView.append(i)
    return preView

#EDITAR motos
def editMoto(i):
    with conexao:
        cur = conexao.cursor()
        querry = "UPDATE motos SET preco=?, kilometragem=?, status=?, dataVenda=? WHERE id=?"
        cur.execute(querry, i)

#DELETAR motos
def deleteMoto(id):
    with conexao:
        cur = conexao.cursor()
        querry = "DELETE FROM motos WHERE id=?"
        cur.execute(querry, id)