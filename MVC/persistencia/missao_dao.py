from MVC.persistencia.abstract_dao import DAO
from MVC.entidade.missao import Missao


class MissaoDAO(DAO):

    def __init__(self):
        super().__init__('missao.pkl')

    def persist(self, missao: Missao):
        if self.__missao_valida(missao):
            super().persist(missao.titulo, missao)

    def remove(self, missao: Missao):
        if self.__missao_valida(missao):
            super().remove(missao.titulo)

    def __missao_valida(self, missao):
        return ((missao is not None) and (isinstance(missao, Missao)) and (isinstance(missao.titulo, str)))
