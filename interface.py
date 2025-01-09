import _mysql_connector

conexao = _mysql_connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='dbveiculos',
)
cursor = conexao.cursor()

''' CREATE
comando = f'INSERT INTO carros () VALUES({}, {})'
cursor.execute(comando)
conexao.commit()
'''

'''READ
comando = 'SELECT * FROM carros'
resustado = cursor.fetchall()
print(resultado)
'''

'''UPDATE
comando = f'UPDATE carros SET tanana WHERE placa = {placa}'
cursor.execute(comando)
conexao.commit()
'''

'''DELETE
comando = f'DELETE FROM carros WHERE placa = {placa}'
cursor.execute(comando)
conexao.commit()
'''

cursor.close()
conexao.close()