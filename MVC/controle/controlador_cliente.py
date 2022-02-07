from MVC.limite.tela_cliente import TelaCliente
from MVC.entidade.cliente import Cliente


class ControladorCliente:
    def __init__(self, controlador_sistema):
        self.__clientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente(self)

    @property
    def clientes(self):
        return self.__clientes

    def pega_cliente_por_codigo(self, codigo: int):
        for cliente in self.__clientes:
            if cliente.codigo == codigo:
                return cliente
        return None

    def seleciona_cliente(self):
        self.__tela_cliente.mostra_lista_clientes(self.__clientes)
        codigo = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_codigo(codigo)
        if cliente is not None:
            return cliente

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados_cliente["nome"], dados_cliente["pais_origem"], dados_cliente["local_sede"],
                          dados_cliente["codigo"])
        self.__clientes.append(cliente)

    def alterar_cliente(self):
        if self.__clientes == []:
            self.__tela_cliente.mostra_mensagem("\033[1;31mATENÇÃO: Ainda não há clientes cadastrados.\033[0m")
            print()
            self.abre_tela()
        self.lista_clientes()
        codigo_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_codigo(codigo_cliente)

        if cliente is not None:
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente.nome = novos_dados_cliente["nome"]
            cliente.pais_origem = novos_dados_cliente["pais_origem"]
            cliente.local_sede = novos_dados_cliente["local_sede"]
            cliente.codigo = novos_dados_cliente["codigo"]
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem("ATENCAO: cliente não existente")

    def lista_clientes(self):
        if len(self.__clientes) == 0:
            return self.__tela_cliente.mostra_mensagem("\033[1;31mATENÇÃO: A lista de clientes está vazia\033[0m")
        for cliente in self.__clientes:
            self.__tela_cliente.mostra_cliente({"nome": cliente.nome, "pais_origem": cliente.pais_origem,
                                                "local_sede": cliente.local_sede, "codigo": cliente.codigo})

    def checar_lista_clientes(self):
        if len(self.__clientes) == 0:
            return 0

    def deseja_mais(self):
        pergunta = self.__tela_cliente.deseja_mais()
        return pergunta

    def excluir_cliente(self):
        if self.__clientes == []:
            self.__tela_cliente.mostra_mensagem("\033[1;31mATENÇÃO: Ainda não há clientes cadastrados.\033[0m")
            print()
            self.abre_tela()
        self.lista_clientes()
        codigo_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_codigo(codigo_cliente)

        if cliente is not None:
            self.__clientes.remove(cliente)
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem("ATENÇÃO: Cliente não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.lista_clientes,
                        4: self.excluir_cliente,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
