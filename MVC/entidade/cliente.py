class Cliente:
    def __init__(self, nome: str, pais_origem: str, local_sede: str):
        self.__nome = nome
        self.__pais_origem = pais_origem
        self.__local_sede = local_sede

    @property
    def nome(self):
        return self.__nome

    @property
    def pais_origem(self):
        return self.__pais_origem

    @property
    def local_sede(self):
        return self.__local_sede

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @pais_origem.setter
    def pais_origem(self, pais_origem: str):
        self.__pais_origem = pais_origem

    @local_sede.setter
    def local_sede(self, local_sede: str):
        self.__local_sede = local_sede
