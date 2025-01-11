import sqlite3 as lite

con = lite.connect('veiculos.db')

with con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca VARCHAR(45) NOT NULL,
        modelo VARCHAR(100) NOT NULL,
        anoFabricacao DATE NOT NULL,
        preco DECIMAL(10,2) NOT NULL,
        cor VARCHAR(45),
        placa VARCHAR(7) NOT NULL,
        chassis VARCHAR(17) NOT NULL,
        numeroMotor VARCHAR(17) NOT NULL,
        kilometragem INT NOT NULL,
        tipoCombustivel VARCHAR(45),
        cilindradas INT,
        potencia VARCHAR(10),
        tipoTransmicao VARCHAR(45),
        status VARCHAR(45) NOT NULL,
        dataVenda DATE,
        numeroPortas INT,
        airbags INT,
        tipoDirecao VARCHAR(45),
        tracao VARCHAR(45),
        espacoPortaMalas INT
    )
    ''')
    cur.execute('''
    CREATE TABLE motos (
        id INTEGER PRIMARY KEY autoincrement,
        marca VARCHAR(45) NOT NULL,
        modelo VARCHAR(100) NOT NULL,
        anoFabricacao DATE NOT NULL,
        preco DECIMAL(10,2) NOT NULL,
        cor VARCHAR(45),
        placa VARCHAR(7) NOT NULL,
        chassis VARCHAR(17) NOT NULL,
        numeroMotor VARCHAR(17) NOT NULL,
        kilometragem INT NOT NULL,
        tipoCombustivel VARCHAR(45),
        cilindradas INT,
        potencia VARCHAR(10),
        tipoTransmicao VARCHAR(45),
        status VARCHAR(45) NOT NULL,
        dataVenda DATE,
        tipoMoto VARCHAR(45),
        peso INT,
        tipoFreio VARCHAR(45),
        acessoriosEspeciais VARCHAR(100)
    )
    ''')
