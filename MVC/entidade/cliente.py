class Cliente:
    def __init__(self, nome: str, pais_origem: str, local_sede: str, codigo: int):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(pais_origem, str):
            self.__pais_origem = pais_origem
        if isinstance(local_sede, str):
            self.__local_sede = local_sede
        if isinstance(codigo, int):
            self.__codigo = codigo

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
        if isinstance(nome, str):
            self.__nome = nome

    @pais_origem.setter
    def pais_origem(self, pais_origem: str):
        if isinstance(pais_origem, str):
            self.__pais_origem = pais_origem

    @local_sede.setter
    def local_sede(self, local_sede: str):
        self.__local_sede = local_sede

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo
