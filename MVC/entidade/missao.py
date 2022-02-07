class Missao:
    def __init__(self, titulo: str, data: str, local: str, conflito: str, clientes: list, tarefas: list,
                 super_herois: list, viloes: list,
                 resultado=None):
        self.__titulo = titulo
        self.__data = data
        self.__local = local
        self.__conflito = conflito
        self.__clientes = clientes
        self.__tarefas = tarefas
        self.__super_herois = super_herois
        self.__viloes = viloes
        self.__resultado = resultado

    @property
    def titulo(self):
        return self.__titulo

    @property
    def data(self):
        return self.__data

    @property
    def local(self):
        return self.__local

    @property
    def conflito(self):
        return self.__conflito

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tarefas(self):
        return self.__tarefas

    @property
    def super_herois(self):
        return self.__super_herois

    @property
    def viloes(self):
        return self.__viloes

    @property
    def resultado(self):
        return self.__resultado

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @data.setter
    def data(self, data: str):
        self.__data = data

    @local.setter
    def local(self, local: str):
        self.__local = local

    @conflito.setter
    def conflito(self, conflito: str):
        self.__conflito = conflito

    @clientes.setter
    def clientes(self, clientes: list):
        self.__clientes = clientes

    @tarefas.setter
    def tarefas(self, tarefas: list):
        self.__tarefas = tarefas

    @super_herois.setter
    def super_herois(self, super_herois):
        self.__super_herois = super_herois

    @viloes.setter
    def viloes(self, viloes):
        self.__viloes = viloes

    @resultado.setter
    def resultado(self, resultado: str):
        self.__resultado = resultado
