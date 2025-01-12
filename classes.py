from main import conexao

class Veiculo:
    def __init__(self, marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status):
        self.marca=marca
        self.modelo=modelo
        self.anoDeFabricacao=anoDeFabricacao
        self.preco=preco
        self.cor=cor
        self.placa=placa
        self.numeroChassis=numeroChassis
        self.numeroMotor=numeroMotor
        self.kilometragem=kilometragem
        self.tipoCombustivel=tipoCombustivel
        self.cilindradas=cilindradas
        self.potencia=potencia
        self.tipoTransmicao=tipoTransmicao
        self.status=status
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status, numeroPortas, airbags, tipoDirecao, tracao, espacoPortaMalas):
        super().__init__(marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status)
        self.numeroPortas=numeroPortas
        self.airbags=airbags
        self.tipoDirecao=tipoDirecao
        self.tracao=tracao
        self.espacoPortaMalas=espacoPortaMalas     

    def __str__(self):
        return str([self.marca, self.modelo, self.anoDeFabricacao, self.preco, self.cor, self.placa, self.numeroChassis, self.numeroMotor, self.kilometragem, self.tipoCombustivel, self.cilindradas, self.potencia, self.tipoTransmicao, self.status, self.numeroPortas, self.airbags, self.tipoDirecao, self.tracao, self.espacoPortaMalas])

    def insertCarro(self):
        with conexao:
            cur = conexao.cursor()
            query = f'''INSERT INTO carros (marca, modelo, anoFabricacao, preco, cor,
                                            placa, chassis, numeroMotor, kilometragem, tipoCombustivel,
                                            cilindradas, potencia, tipoTransmicao, status, dataVenda,
                                            numeroPortas, airbags, tipoDirecao, tracao, espacoPortaMalas) 
                                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, Null, ?, ?, ?, ?, ?)'''
            cur.execute(query, [self.marca, self.modelo, self.anoDeFabricacao, self.preco, self.cor, self.placa, self.numeroChassis, self.numeroMotor, self.kilometragem, self.tipoCombustivel, self.cilindradas, self.potencia, self.tipoTransmicao, self.status, self.numeroPortas, self.airbags, self.tipoDirecao, self.tracao, self.espacoPortaMalas])

class Moto(Veiculo):
    def __init__(self, marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status, tipoMoto, peso, tipoFreio, acessoriosEspeciais, ):
        super().__init__(marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status)
        self.tipoMoto=tipoMoto
        self.peso=peso
        self.tipoFreio=tipoFreio
        self.acessoriosEspeciais=acessoriosEspeciais

    def __str__(self):
        return str([self.marca,self.modelo,self.anoDeFabricacao,self.preco,self.cor,self.placa,self.numeroChassis,self.numeroMotor,self.kilometragem,self.tipoCombustivel,self.cilindradas,self.potencia,self.tipoTransmicao,self.status,self.tipoMoto,self.peso,self.tipoFreio,self.acessoriosEspeciais])

    def insertMoto(self):
        with conexao:
            cur = conexao.cursor()
            query = f'''INSERT INTO motos (marca, modelo, anoFabricacao, preco, cor,
                                            placa, chassis, numeroMotor, kilometragem, tipoCombustivel,
                                            cilindradas, potencia, tipoTransmicao, status, dataVenda,
                                            tipoMoto, peso, tipoFreio, acessoriosEspeciais) 
                                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, Null, ?, ?, ?, ?)'''
            cur.execute(query, [self.marca,self.modelo,self.anoDeFabricacao,self.preco,self.cor,self.placa,self.numeroChassis,self.numeroMotor,self.kilometragem,self.tipoCombustivel,self.cilindradas,self.potencia,self.tipoTransmicao,self.status,self.tipoMoto,self.peso,self.tipoFreio,self.acessoriosEspeciais])