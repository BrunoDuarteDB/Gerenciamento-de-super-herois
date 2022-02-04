from MVC.limite.tela_senciente import TelaSenciente
from MVC.entidade.senciente import Senciente
from MVC.entidade.super_heroi import SuperHeroi
from MVC.entidade.vilao import Vilao

class ControladorSenciente:

    def __init__(self, controlador_sistema):
        self.__super_herois = []
        self.__viloes = []
        self.__tela_senciente = TelaSenciente(self)
        self.__controlador_sistema = controlador_sistema

    def pega_senciente_por_nome(self, nome: str):
        for senciente in self.__super_herois:
            if senciente.nome == nome:
                return senciente
        for senciente in self.__viloes:
            if senciente.nome == nome:
                return senciente
        return None

    def pede_cadastro_poder(self):
        self.__controlador_sistema.controlador_poder.inclui_poder()

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

    def seleciona_super_heroi(self):
        self.__tela_senciente.mostra_lista_super_herois(self.__super_herois)
        nome = self.__tela_senciente.seleciona_super_heroi()
        super_heroi = self.__controlador_senciente.pega_senciente_por_nome(nome)
        if super_heroi is not None:
            return super_heroi

    def seleciona_vilao(self):
        self.__tela_senciente.mostra_lista_viloes(self.__viloes)
        nome = self.__tela_senciente.seleciona_vilao()
        vilao = self.__controlador_senciente.pega_senciente_por_nome(nome)
        if vilao is not None:
            return vilao

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

    def inclui_poder_em_senciente(self):
        poder = self.__cadastra_poder()
        return poder

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_senciente, 2: self.alterar_senciente, 3: self.listar_senciente,
                        4: self.excluir_senciente, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_senciente.tela_opcoes()]()