from limite.tela_sistema import TelaSistema
from controle.controlador_missao import ControladorMissao
from controle.controlador_senciente import ControladorSenciente
from controle.controlador_poder import ControladorPoder
from controle.controlador_cliente import ControladorCliente

class ControladorSistema:

    def __init__(self):
        self.__controlador_missao = ControladorMissao(self)
        self.__controlador_senciente = ControladorSenciente(self)
        self.__controlador_poder = ControladorPoder(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_missao(self):
        return self.__controlador_missao

    @property
    def controlador_senciente(self):
        return self.__controlador_senciente

    @property
    def controlador_poder(self):
        return self.__controlador_poder

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_missao(self):
        self.__controlador_missao.abre_tela()

    def cadastra_senciente(self):
        self.__controlador_senciente.abre_tela()

    def cadastra_poder(self):
        self.__controlador_poder.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_missao, 2: self.cadastra_senciente, 3: self.cadastra_poder,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
