from MVC.entidade.senciente import Senciente


class Vilao(Senciente):
    def __init__(self, nome: str, poder, fraqueza: str, empresa: str, local_moradia: str, periculosidade: int):
        super().__init__(nome, poder, fraqueza, empresa, local_moradia)
        if isinstance(periculosidade, int):
            self.__periculosidade = periculosidade

    @property
    def periculosidade(self):
        return self.__periculosidade

    @periculosidade.setter
    def periculosidade(self, periculosidade: int):
        if isinstance(periculosidade, int):
            self.__periculosidade = periculosidade
