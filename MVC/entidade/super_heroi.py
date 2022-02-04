from entidade.senciente import Senciente
from entidade.poder import Poder

class SuperHeroi(Senciente):
    def __init__(self, nome: str, poder: Poder, fraqueza: str, empresa: str, local_moradia: str, alterego: str):
        super().__init__(nome, poder, fraqueza, empresa, local_moradia)
        self.__alterego = alterego

    @property
    def alterego(self):
        return self.__alterego

    @alterego.setter
    def alterego(self, alterego):
        self.__alterego = alterego

