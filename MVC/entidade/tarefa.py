class Tarefa:
    def __init__(self, id_tarefa: int, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(id_tarefa, int):
            self.__id_tarefa = id_tarefa

    @property
    def id_tarefa(self):
        return self.__id_tarefa

    @id_tarefa.setter
    def id_tarefa(self, id_tarefa: int):
        if isinstance(id_tarefa, int):
            self.__id_tarefa = id_tarefa

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
