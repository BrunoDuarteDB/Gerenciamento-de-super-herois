from abc import ABC, abstractmethod
from MVC.entidade.poder import Poder


class Senciente(ABC):
    @abstractmethod
    def __init__(self, nome: str, poder: Poder, fraqueza: str, empresa: str, local_moradia: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(poder, Poder):
            self.__poder = poder
        if isinstance(fraqueza, str):
            self.__fraqueza = fraqueza
        if isinstance(empresa, str):
            self.__empresa = empresa
        if isinstance(local_moradia, str):
            self.__local_moradia = local_moradia

    @property
    def nome(self):
        return self.__nome

    @property
    def poder(self):
        return self.__poder

    @property
    def fraqueza(self):
        return self.__fraqueza

    @property
    def empresa(self):
        return self.__empresa

    @property
    def local_moradia(self):
        return self.__local_moradia

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @poder.setter
    def poder(self, poder):
        if isinstance(poder, Poder):
            self.__poder = poder

    @fraqueza.setter
    def fraqueza(self, fraqueza):
        if isinstance(fraqueza, str):
            self.__fraqueza = fraqueza

    @empresa.setter
    def empresa(self, empresa):
        if isinstance(empresa, str):
            self.__empresa = empresa

    @local_moradia.setter
    def local_moradia(self, local_moradia):
        if isinstance(local_moradia, str):
            self.__local_moradia = local_moradia
