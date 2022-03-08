class Missao:
    def __init__(self, titulo: str, data: str, local: str, conflito: str, clientes: list, tarefas: list,
                 super_herois: list, viloes: list,
                 resultado=None):
        # testar tipos!!!
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(data, str):
            self.__data = data
        if isinstance(local, str):
            self.__local = local
        if isinstance(conflito, str):
            self.__conflito = conflito
        if isinstance(clientes, list):
            self.__clientes = clientes
        if isinstance(tarefas, list):
            self.__tarefas = tarefas
        if isinstance(super_herois, list):
            self.__super_herois = super_herois
        if isinstance(viloes, list):
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
        if isinstance(titulo, str):
            self.__titulo = titulo

    @data.setter
    def data(self, data: str):
        if isinstance(data, str):
            self.__data = data

    @local.setter
    def local(self, local: str):
        if isinstance(local, str):
            self.__local = local

    @conflito.setter
    def conflito(self, conflito: str):
        if isinstance(conflito, str):
            self.__conflito = conflito

    @clientes.setter
    def clientes(self, clientes: list):
        if isinstance(clientes, list):
            self.__clientes = clientes

    @tarefas.setter
    def tarefas(self, tarefas: list):
        if isinstance(tarefas, list):
            self.__tarefas = tarefas

    @super_herois.setter
    def super_herois(self, super_herois):
        if isinstance(super_herois, list):
            self.__super_herois = super_herois

    @viloes.setter
    def viloes(self, viloes):
        if isinstance(viloes, list):
            self.__viloes = viloes

    @resultado.setter
    def resultado(self, resultado: str):
        self.__resultado = resultado
