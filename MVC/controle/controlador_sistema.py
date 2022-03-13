from MVC.limite.tela_sistema import TelaSistema
from MVC.limite.tela_sistema_gui import TelaSistemaGUI
from MVC.controle.controlador_missao import ControladorMissao
from MVC.controle.controlador_senciente import ControladorSenciente
from MVC.controle.controlador_poder import ControladorPoder
from MVC.controle.controlador_cliente import ControladorCliente
from MVC.exceptions.missaoSemIntegrantesException import MissaoSemIntegrantesException


class ControladorSistema:

    def __init__(self):
        self.__controlador_missao = ControladorMissao(self)
        self.__controlador_senciente = ControladorSenciente(self)
        self.__controlador_poder = ControladorPoder(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__tela_sistema_gui = TelaSistemaGUI(self)
        # self.__tela_sistema = TelaSistema(self)

    @property
    def controlador_missao(self):
        return self.__controlador_missao

    @property
    def controlador_senciente(self):
        return self.__controlador_senciente

    @property
    def controlador_poder(self):
        return self.__controlador_poder

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_missao(self):
        checagem_super_heroi = self.__controlador_senciente.checar_lista_super_herois()
        checagem_cliente = self.__controlador_cliente.checar_lista_clientes()
        try:
            if checagem_super_heroi == 0 and checagem_cliente == 0:
                raise MissaoSemIntegrantesException()
            self.__controlador_missao.abre_tela()
        except:
            self.__tela_sistema_gui.show_message("Ops!",
                                                 "Você primeiro deve cadastrar pelo menos um Super-Herói e um cliente!")


        '''if checagem_super_heroi != 0 and checagem_cliente != 0:
            self.__controlador_missao.abre_tela()
        else:
            self.__tela_sistema_gui.show_message("Ops!",
                "Você primeiro deve cadastrar pelo menos um Super-Herói e um cliente!")'''

    def cadastra_senciente(self):
        self.__controlador_senciente.abre_tela()
        self.__tela_sistema_gui.close()

    def cadastra_poder(self):
        self.__controlador_poder.abre_tela()
        self.__tela_sistema_gui.close()

    def cadastra_cliente(self):
        self.__controlador_cliente.abre_tela()
        self.__tela_sistema_gui.close()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {'Missão': self.cadastra_missao, 'Senciente (Super-Herói ou Vilão)': self.cadastra_senciente,
                        'Poder': self.cadastra_poder, 'Cliente': self.cadastra_cliente,
                        'Finalizar Sistema': self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema_gui.open()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
