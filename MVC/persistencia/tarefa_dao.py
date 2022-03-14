from MVC.persistencia.abstract_dao import DAO
from MVC.entidade.tarefa import Tarefa


class TarefaDAO(DAO):

    def __init__(self):
        super().__init__('tarefa.pkl')

    def persist(self, tarefa: Tarefa):
        if self.__tarefa_valida(tarefa):
            super().persist(tarefa.id_tarefa, tarefa)

    def remove(self, tarefa: Tarefa):
        if self.__tarefa_valida(tarefa):
            super().remove(tarefa.id_tarefa)

    def __tarefa_valida(self, tarefa):
        return ((tarefa is not None) and (isinstance(tarefa, Tarefa)) and (isinstance(tarefa.id_tarefa, int)))
