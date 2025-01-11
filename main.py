import sqlite3 as lite

conexao = lite.connect('veiculos.db')

#----------------------------------------Carros----------------------------------------#

#CRIAR carros
def incertInfoCarros(i):
#i = ['mitsubishi','l200 triton','2009','80000','azul','mon2025','9BD111060T5002156','9BD111060T5002156','190000','diesel','3200','165cv','manual','em espera','4','2','hidraulica','4x4','1000']
#if i != 0:
    with conexao:
        cur = conexao.cursor()
        query = f'''INSERT INTO carros (marca, modelo, anoFabricacao, preco, cor,
                                        placa, chassis, numeroMotor, kilometragem, tipoCombustivel,
                                        cilindradas, potencia, tipoTransmicao, status, dataVenda,
                                        numeroPortas, airbags, tipoDirecao, tracao, espacoPortaMalas) 
                                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, Null, ?, ?, ?, ?, ?)'''
        cur.execute(query, i)


#VISUALIZAR carros
def viewInfoCarros(id):
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
def preViewInfoCarros():
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
def editInfoCarros():
    lista = ["26000", "187000", "em espera", None, 1]
    with conexao:
        cur = conexao.cursor()
        querry = "UPDATE carros SET preco=?, kilometragem=?, status=?, dataVenda=? WHERE id=?"
        cur.execute(querry, lista)

#DELETAR carros
def deleteInfoCarros(id):
    with conexao:
        cur = conexao.cursor()
        querry = "DELETE FROM carros WHERE id=?"
        cur.execute(querry, id)

#----------------------------------------Motos----------------------------------------#

#CRIAR motos
def incertInfoMotos(i):
#i = ['honda', 'cg 125 today', '1992', '5000', 'vermelha', 'mas2025', '9BD111060T5002156', '9BD111060T5002156', '27000', 'gasolina', '125', '11,5 cv', 'manual', 'em espera', 'triciclo', '300kg', 'tambor', 'kit trilha']
#if i != 0:
    with conexao:
        cur = conexao.cursor()
        query = f'''INSERT INTO motos (marca, modelo, anoFabricacao, preco, cor,
                                        placa, chassis, numeroMotor, kilometragem, tipoCombustivel,
                                        cilindradas, potencia, tipoTransmicao, status, dataVenda,
                                        tipoMoto, peso, tipoFreio, acessoriosEspeciais) 
                                    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, Null, ?, ?, ?, ?)'''
        cur.execute(query, i)

#VISUALIZAR motos
def viewInfoMotos(id):
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
def preViewInfoMotos():
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
def editInfoMotos():
    lista = ["26000", "187000", "em espera", None, 1]
    with conexao:
        cur = conexao.cursor()
        querry = "UPDATE motos SET preco=?, kilometragem=?, status=?, dataVenda=? WHERE id=?"
        cur.execute(querry, lista)

#DELETAR motos
def deleteInfoMotos(id):
    with conexao:
        cur = conexao.cursor()
        querry = "DELETE FROM motos WHERE id=?"
        cur.execute(querry, id)