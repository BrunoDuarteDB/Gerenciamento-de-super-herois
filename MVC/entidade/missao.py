
class Missao:
    def __init__(self, titulo: str, data: str, local: str, conflito: str, resultado=None):  # aqui já não deveria gerar o resultado? MUDAR NO DIAGRAMA
        self.__titulo = titulo
        self.__data = data
        self.__local = local
        self.__conflito = conflito
        self.__clientes = []
        self.__tarefas = []
        self.__super_herois = []
        self.__viloes = [] # MUDAR NO DIAGRAMA
        self.__resultado = None

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

    @resultado.setter
    def resultado(self, resultado: str):
        self.__resultado = resultado

    def incluir_cliente(self, cliente: Cliente):
        pass

    def excluir_cliente(self, cliente: Cliente):
        pass

    def listar_tarefas(self):
        pass

    def incluir_super_heroi(self, super_heroi: SuperHeroi):
        pass

    def excluir_super_heroi(self, super_heroi: SuperHeroi):
        pass

    def listar_super_herois(self):
        pass

    def incluir_vilao(self, vilao: Vilao):
        pass

    def excluir_vilao(self, vilao: Vilao):
        pass

    def listar_viloes(self):
        pass

    def listar_detalhes(self):
        pass
