from MVC.limite.tela_cliente_gui import TelaClienteGUI
from MVC.limite.tela_dados_cliente import TelaDadosCliente
from MVC.entidade.cliente import Cliente
from MVC.exceptions.botaoErradoException import BotaoErradoException
from MVC.persistencia.cliente_dao import ClienteDAO


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente_gui = TelaClienteGUI(self)
        self.__tela_dados_cliente = TelaDadosCliente(self)
        self.__cliente_dao = ClienteDAO()

    @property
    def clientes(self):
        return self.__cliente_dao.get_all()

    def seleciona_cliente(self):
        clientes = []
        dict_clientes = self.monta_dict_clientes()
        button = 'Incluir mais Clientes'
        while button == 'Incluir mais Clientes':

            while True:
                button, values = self.__tela_cliente_gui.open(dict_clientes)

                try:
                    if button != 'Incluir mais Clientes' and button != 'Incluir em Missão':
                        raise BotaoErradoException
                    break
                except BotaoErradoException:
                    self.__tela_cliente_gui.show_message('Ops','Você deve clicar em "Incluir mais Clientes" ou "Incluir'
                                                               'em Missão"!')
                    continue

            self.__tela_cliente_gui.close()
            if values['lb_itens'] != []:
                clientes.append(values['lb_itens'])
        return clientes

    def incluir_cliente(self, values=None):
        while True:
            botao, dados_cliente = self.__tela_dados_cliente.open(dados_cliente={"codigo":"","nome":"","pais_origem":"",
                                                                                 "local_sede":""})

            print(botao, dados_cliente)
            self.__tela_dados_cliente.close()

            try:
                int(dados_cliente["codigo"])
                if dados_cliente == {"codigo":"","nome":"","pais_origem":"","local_sede":""} or \
                        (dados_cliente["nome"]).isdigit() == True or (dados_cliente["pais_origem"]).isdigit() == True \
                        or (dados_cliente["local_sede"]).isdigit() == True:
                    raise ValueError
                cliente = Cliente(dados_cliente["nome"], dados_cliente["pais_origem"], dados_cliente["local_sede"],
                                  int(dados_cliente["codigo"]))
                self.__cliente_dao.persist(cliente)
                self.__tela_cliente_gui.close()
                break
            except ValueError:
                self.__tela_cliente_gui.show_message('Atenção', 'Código inválido, tente novamente!')
                continue

    def monta_dict_clientes(self):
        clientes = []
        for cliente in self.__cliente_dao.get_all():
            clientes.append(cliente.nome)
        return clientes

    def alterar_cliente(self, dados_cliente):
        if self.__cliente_dao.get_all() == []:
            self.__tela_cliente_gui.show_message("Atenção!", "Ainda não há clientes cadastrados.")

        nome_cliente_alterado = dados_cliente['lb_itens'][0]

        for cliente in self.__cliente_dao.get_all():
            if cliente.nome == nome_cliente_alterado:
                dados_cliente = {"codigo": cliente.codigo, "nome": cliente.nome, "pais_origem": cliente.pais_origem,
                                 "local_sede": cliente.local_sede}

        while True:
            try:
                button, values = self.__tela_dados_cliente.open(dados_cliente)
                self.__tela_dados_cliente.close()
                int(values["codigo"])
                if values == {"codigo": "", "nome": "", "pais_origem": "", "local_sede": ""} or \
                        (values["nome"]).isdigit() == True or (values["pais_origem"]).isdigit() == True \
                        or (dados_cliente["local_sede"]).isdigit() == True:
                    raise ValueError
                for cliente in self.__cliente_dao.get_all():
                    if cliente.nome == nome_cliente_alterado:
                        cliente.nome = values["nome"]
                        cliente.pais_origem = values["pais_origem"]
                        cliente.local_sede = values["local_sede"]
                        cliente.codigo = values["codigo"]

                        self.__cliente_dao.persist(cliente) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                break
            except ValueError:
                self.__tela_cliente_gui.show_message('Atenção', 'Código inválido, tente novamente!')
                continue

        self.__tela_dados_cliente.close()
        self.__tela_cliente_gui.close()

    def checar_lista_clientes(self):
        clientes = []
        for cliente in self.__cliente_dao.get_all():
            clientes.append(cliente)
        if clientes == []:
            return 0

    def deseja_mais(self):
        pergunta = self.__tela_cliente.deseja_mais()
        return pergunta

    def excluir_cliente(self, dados_cliente):
        if self.__cliente_dao.get_all() == []:
            self.__tela_cliente_gui.show_message("Atenção!", "Ainda não há clientes cadastrados.")

        nome_cliente_excluido = dados_cliente['lb_itens'][0]

        lista_clientes = self.__cliente_dao.get_all()
        cliente_excluido = ''
        for cliente in lista_clientes:
            if cliente.nome == nome_cliente_excluido:
                cliente_excluido = cliente
        self.__cliente_dao.remove(cliente_excluido)
        del cliente_excluido
        self.__tela_cliente_gui.close()

    def retornar(self, values):
        self.__tela_cliente_gui.close()
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {'Novo Cliente': self.incluir_cliente, 'Alterar': self.alterar_cliente, # 3: self.lista_clientes,
                        'Excluir': self.excluir_cliente, 'Retornar': self.retornar}

        continua = True
        while continua:
            dict_clientes = self.monta_dict_clientes()
            button, values = self.__tela_cliente_gui.open(dict_clientes)
            lista_opcoes[button](values)

            # lista_opcoes[self.__tela_cliente_gui.open(self.monta_dict_clientes())]()
