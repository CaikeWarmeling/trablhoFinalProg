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

class Moto(Veiculo):
    def __init__(self, marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status, tipoMoto, peso, tipoFreio, acessoriosEspeciais, ):
        super().__init__(marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status)
        self.tipoMoto=tipoMoto
        self.peso=peso
        self.tipoFreio=tipoFreio
        self.acessoriosEspeciais=acessoriosEspeciais