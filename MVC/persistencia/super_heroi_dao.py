from MVC.persistencia.abstract_dao import DAO
from MVC.entidade.super_heroi import SuperHeroi


class SuperHeroiDAO(DAO):

    def __init__(self):
        super().__init__('super_heroi.pkl')

    def persist(self, super_heroi: SuperHeroi):
        if self.__super_heroi_valido(super_heroi):
            super().persist(super_heroi.nome, super_heroi)

    def remove(self, super_heroi: SuperHeroi):
        if self.__super_heroi_valido(super_heroi):
            super().remove(super_heroi.nome)

    def __super_heroi_valido(self, super_heroi):
        return ((super_heroi is not None) and (isinstance(super_heroi, SuperHeroi)) and (
            isinstance(super_heroi.nome, str)))
