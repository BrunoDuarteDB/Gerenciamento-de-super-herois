from MVC.limite.tela_sistema import TelaSistema
from MVC.controle.controlador_missao import ControladorMissao
from MVC.controle.controlador_senciente import ControladorSenciente
from MVC.controle.controlador_poder import ControladorPoder
from MVC.controle.controlador_cliente import ControladorCliente

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

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_missao(self):
        checagem = self.__controlador_senciente.checar_lista_super_herois()
        if checagem is None:
            self.__tela_sistema.mostrar_mensagem('Ops, você primeiro deve cadastrar pelo menos um Super-Herói!')
        else:
            self.__controlador_missao.abre_tela()

    def cadastra_senciente(self):
        self.__controlador_senciente.abre_tela()

    def cadastra_poder(self):
        self.__controlador_poder.abre_tela()

    def cadastra_cliente(self):
        self.__controlador_cliente.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_missao, 2: self.cadastra_senciente, 3: self.cadastra_poder,
                        4: self.cadastra_cliente, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
