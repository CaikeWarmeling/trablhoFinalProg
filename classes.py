class Veiculo:
    def __init__(self, marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status, dataVenda):
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
        self.dataVenda=dataVenda

    @property
    def placa(self):
        return self.__placa
        
    @placa.setter
    def cpf(self, nova_placa):
        self.__placa = nova_placa

    @property
    def numeroChassis(self):
        return self.__numeroChassis
        
    @numeroChassis.setter
    def cpf(self, novo_numeroChassis):
        self.__numeroChassis = novo_numeroChassis

    @property
    def numeroMotor(self):
        return self.__numeroMotor
        
    @numeroMotor.setter
    def cpf(self, novo_numeroMotor):
        self.__numeroMotor = novo_numeroMotor

class Carro(Veiculo):
    def __init__(self, marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status, dataVenda, numeroPortas, airbags, tipoDirecao, tracao, espacoPortaMalas):
        super().__init__(self, marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status, dataVenda)
        self.numeroPortas=numeroPortas
        self.airbags=airbags
        self.tipoDirecao=tipoDirecao
        self.tracao=tracao
        self.espacoPortaMalas=espacoPortaMalas

class Moto(Veiculo):
    def __init__(self, marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status, dataVenda, tipoMoto, peso, tipoFreio, acessoriosEspeciais, ):
        super().__init__(marca, modelo, anoDeFabricacao, preco, cor, placa, numeroChassis, numeroMotor, kilometragem, tipoCombustivel, cilindradas, potencia, tipoTransmicao, status, dataVenda)
        self.tipoMoto=tipoMoto
        self.peso=peso
        self.tipoFreio=tipoFreio
        self.acessoriosEspeciais=acessoriosEspeciais