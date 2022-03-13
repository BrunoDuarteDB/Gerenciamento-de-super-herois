from MVC.persistencia.abstract_dao import DAO
from MVC.entidade.poder import Poder


class PoderDAO(DAO):

    def __init__(self):
        super().__init__('poder.pkl')

    def persist(self, poder: Poder):
        if self.__poder_valido(poder):
            super().persist(poder.detentor, poder)

    def remove(self, poder: Poder):
        if self.__poder_valido(poder):
            super().remove(poder.detentor)

    def __poder_valido(self, poder):
        return ((poder is not None) and (isinstance(poder, Poder)) and (isinstance(poder.detentor, str)))
