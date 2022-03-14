from MVC.persistencia.abstract_dao import DAO
from MVC.entidade.vilao import Vilao

class VilaoDAO(DAO):

    def __init__(self):
        super().__init__('vilao.pkl')

    def persist(self, vilao: Vilao):
        if self.__vilao_valido(vilao):
            super().persist(vilao.nome, vilao)

    def remove(self, vilao: Vilao):
        if self.__vilao_valido(vilao):
            super().remove(vilao.nome)

    def __vilao_valido(self, vilao):
        return ((vilao is not None) and (isinstance(vilao, Vilao)) and (isinstance(vilao.nome, str)))