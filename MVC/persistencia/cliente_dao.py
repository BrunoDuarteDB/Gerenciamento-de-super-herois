from MVC.persistencia.abstract_dao import DAO
from MVC.entidade.cliente import Cliente

class ClienteDAO(DAO):

    def __init__(self):
        super().__init__('cliente.pkl')

    def persist(self, cliente:Cliente):
        if self.__cliente_valido(cliente):
            super().persist(cliente.codigo, cliente)

    def remove(self, cliente: Cliente):
        if self.__cliente_valido(cliente):
            super().remove(cliente.codigo)

    def __cliente_valido(self, cliente):
        return ((cliente is not None) and (isinstance(cliente, Cliente)) and (isinstance(cliente.codigo, int)))

