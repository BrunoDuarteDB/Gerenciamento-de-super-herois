from limite.tela_senciente import TelaSenciente
from entidade.senciente import Senciente
from entidade.super_heroi import SuperHeroi
from entidade.vilao import Vilao

class ControladorSenciente():

    def __init__(self):
        self.__super_herois = []
        self.__viloes = []
        self.__tela_senciente = TelaSenciente()
        self.__controlador_sistema = controlador_sistema

    def incluir_senciente(self):
        dados_senciente = self.__tela_senciente.pega_dados_senciente()
        if dados_senciente['heroi_ou_vilao'] == 1:
            senciente = SuperHeroi(dados_senciente['nome'], dados_senciente['poder'], dados_senciente['fraqueza'],
                                   dados_senciente['empresa'], dados_senciente['local_moradia'])
        elif dados_senciente['heroi_ou_vilao'] == 2:
            senciente = Vilao(dados_senciente['nome'], dados_senciente['poder'], dados_senciente['fraqueza'],
                                   dados_senciente['empresa'], dados_senciente['local_moradia'])

    def alterar_senciente(self):
        pass

    def listar_senciente(self):
        pass

    def excluir_senciente(self):
        pass