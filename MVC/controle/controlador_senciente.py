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

    def pega_senciente_por_nome(self, nome: str):
        for senciente in self.__super_herois:
            if senciente.nome == nome:
                return senciente
        for senciente in self.__viloes:
            if senciente.nome == nome:
                return senciente
        return None

    def incluir_senciente(self):
        dados_senciente = self.__tela_senciente.pega_dados_senciente()
        if dados_senciente['heroi_ou_vilao'] == 1:
            senciente = SuperHeroi(dados_senciente['nome'], dados_senciente['poder'], dados_senciente['fraqueza'],
                                   dados_senciente['empresa'], dados_senciente['local_moradia'])
            self.__super_herois.append(senciente)
        elif dados_senciente['heroi_ou_vilao'] == 2:
            senciente = Vilao(dados_senciente['nome'], dados_senciente['poder'], dados_senciente['fraqueza'],
                                   dados_senciente['empresa'], dados_senciente['local_moradia'])
            self.__viloes.append(senciente)

    def alterar_senciente(self):
        self.listar_senciente()
        nome_senciente = self.__tela_senciente.seleciona_senciente()
        senciente = self.pega_senciente_por_nome(nome_senciente)

        if senciente is not None:
            novos_dados_senciente = self.__tela_senciente.pega_dados_senciente()
            senciente.nome = novos_dados_senciente['nome']
            senciente.poder = novos_dados_senciente['poder']
            senciente.fraqueza = novos_dados_senciente['fraqueza']
            senciente.empresa = novos_dados_senciente['empresa']
            senciente.local_moradia = novos_dados_senciente['local_moradia']

            if isinstance(novos_dados_senciente, SuperHeroi):
                senciente.alterego = novos_dados_senciente['alterego']
            elif isinstance(novos_dados_senciente, Vilao):
                senciente.periculosidade = novos_dados_senciente['periculosidade']
        else:
            self.__tela_senciente.mostra_mensagem("Atenção: senciente não existente!")

    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def listar_senciente(self):
        self.__tela_senciente.mostra_mensagem("----- Lista de Super-Heróis -----")
        for senciente in self.__super_herois:
            self.__tela_senciente.mostra_senciente({'nome': senciente.nome,
                                                    'fraqueza': senciente.fraqueza,
                                                    'empresa': senciente.empresa,
                                                    'local_moradia': senciente.local_moradia,
                                                    'alterego': senciente.alterego})
        print('\n')
        self.__tela_senciente.mostra_mensagem("----- Lista de Vilões -----")
        for senciente in self.__viloes:
            self.__tela_senciente.mostra_senciente({'nome': senciente.nome,
                                                    'fraqueza': senciente.fraqueza,
                                                    'empresa': senciente.empresa,
                                                    'local_moradia': senciente.local_moradia,
                                                    'periculosidade': senciente.periculosidade})

    def excluir_senciente(self):
        self.listar_senciente()
        nome_senciente = self.__tela_senciente.seleciona_senciente()
        senciente = self.pega_senciente_por_nome(nome_senciente)

        if senciente is not None:
            if isinstance(senciente, SuperHeroi):
                self.__super_herois.remove(senciente)
            elif isinstance(senciente, Vilao):
                self.__viloes.remove(senciente)
            self.listar_senciente()
        else:
            self.__tela_senciente.mostra_mensagem("Atenção: senciente não existente!")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_senciente, 2: self.alterar_senciente, 3: self.listar_senciente,
                        4: self.excluir_senciente, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_senciente.tela_opcoes()]()