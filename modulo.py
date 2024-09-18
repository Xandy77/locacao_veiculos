class Usuario:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento
        self.veiculo_alugado = None

    @property
    def nome(self):
        return self.__nome

    @property
    def documento(self):
        return self.__documento

    def alugar_veiculo(self, veiculo):
        self.veiculo_alugado = veiculo

    def exibir_dados(self):
        return f'Usuário: {self.nome}, Documento: {self.documento}, Veículo alugado: {self.veiculo_alugado.nome if self.veiculo_alugado else "Nenhum"}'


class Veiculo:
    def __init__(self, nome, modelo, ano, valor_diaria):
        self.__nome = nome
        self.__modelo = modelo
        self.__ano = ano
        self.__valor_diaria = valor_diaria

    @property
    def nome(self):
        return self.__nome

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def valor_diaria(self):
        return self.__valor_diaria

    def exibir_informacoes(self):
        return f'Veículo: {self.nome}, Modelo: {self.modelo}, Ano: {self.ano}, Valor diária: R${self.valor_diaria:.2f}'
