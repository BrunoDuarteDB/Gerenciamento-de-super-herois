from MVC.limite.tela_senciente import TelaSenciente
from MVC.entidade.super_heroi import SuperHeroi
from MVC.entidade.vilao import Vilao
from MVC.limite.tela_senciente_gui import TelaSencienteGUI
from MVC.limite.tela_dados_super_heroi import TelaDadosSuperHeroi
from MVC.limite.tela_dados_vilao import TelaDadosVilao


class ControladorSenciente:

    def __init__(self, controlador_sistema):
        self.__super_herois = []
        self.__viloes = []
        # self.__tela_senciente = TelaSenciente(self)
        self.__tela_senciente_gui = TelaSencienteGUI(self)  #  tem que ajustar
        self.__tela_dados_super_heroi = TelaDadosSuperHeroi(self)
        self.__tela_dados_vilao = TelaDadosVilao(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def super_herois(self):
        return self.__super_herois

    @property
    def viloes(self):
        return self.__viloes

    def pega_senciente_por_nome(self, nome: str):
        for senciente in self.__super_herois:
            if senciente.nome == nome:
                return senciente
        for senciente in self.__viloes:
            if senciente.nome == nome:
                return senciente
        return None

    def pede_cadastro_poder(self, nome):
        poder = self.__controlador_sistema.controlador_poder.inclui_poder(nome)
        return poder

    '''def incluir_senciente(self):
        dados_senciente = self.__tela_senciente.pega_dados_senciente()
        if dados_senciente['heroi_ou_vilao'] == 1:
            senciente = SuperHeroi(dados_senciente['nome'], dados_senciente['poder'], dados_senciente['fraqueza'],
                                   dados_senciente['empresa'], dados_senciente['local_moradia'],
                                   dados_senciente['alterego'])
            self.__super_herois.append(senciente)
        elif dados_senciente['heroi_ou_vilao'] == 2:
            senciente = Vilao(dados_senciente['nome'], dados_senciente['poder'], dados_senciente['fraqueza'],
                              dados_senciente['empresa'], dados_senciente['local_moradia'],
                              dados_senciente['periculosidade'])
            self.__viloes.append(senciente)'''

    def incluir_super_heroi(self, values):
        button, values = self.__tela_dados_super_heroi.open()
        poder = self.__controlador_sistema.controlador_poder.inclui_poder(values['nome'])
        senciente = SuperHeroi(values['nome'], poder, values['fraqueza'],
                                values['empresa'], values['local_moradia'],
                                values['alterego'])
        self.__super_herois.append(senciente)

    def incluir_vilao(self, values):
        button, values = self.__tela_dados_vilao.open()
        poder = self.__controlador_sistema.controlador_poder.inclui_poder(values['nome'])
        senciente = Vilao(values['nome'], poder, values['fraqueza'],
                               values['empresa'], values['local_moradia'],
                               values['periculosidade'])
        self.__viloes.append(senciente)

    def monta_dict_super_herois(self):
        super_herois = []
        for super_heroi in self.__super_herois:
            super_herois.append({"nome": super_heroi.nome, "fraqueza": super_heroi.fraqueza,
                                 "empresa": super_heroi.empresa, "local_moradia": super_heroi.local_moradia,
                                 "alterego": super_heroi.alterego})
            return super_herois

    def monta_dict_viloes(self):
        viloes = []
        for vilao in self.__viloes:
            viloes.append({"nome": vilao.nome, "fraqueza": vilao.fraqueza,
                                 "empresa": vilao.empresa, "local_moradia": vilao.local_moradia,
                                 "periculosidade": vilao.periculosidade})
            return viloes

    def seleciona_super_heroi(self):
        self.__tela_senciente.mostra_lista_super_herois(self.__super_herois)
        nome = self.__tela_senciente.seleciona_super_heroi()
        super_heroi = self.pega_senciente_por_nome(nome)
        if super_heroi is not None:
            return super_heroi

    def seleciona_vilao(self):
        self.__tela_senciente.mostra_lista_viloes(self.__viloes)
        nome = self.__tela_senciente.seleciona_vilao()
        vilao = self.pega_senciente_por_nome(nome)
        if vilao is not None:
            return vilao

    def alterar_senciente(self):
        if self.__viloes == [] and self.__super_herois == []:
            self.__tela_senciente.mostra_mensagem("\033[1;31mATENÇÃO: Ainda não há sencientes cadastrados.\033[0m")
            print()
            self.abre_tela()
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

    def listar_senciente(self):
        if self.__super_herois is not None:
            self.__tela_senciente.mostra_mensagem("----- Lista de Super-Heróis -----")
            for senciente in self.__super_herois:
                self.__tela_senciente.mostra_senciente({'codigo': 1,
                                                        'nome': senciente.nome,
                                                        'fraqueza': senciente.fraqueza,
                                                        'empresa': senciente.empresa,
                                                        'local_moradia': senciente.local_moradia,
                                                        'alterego': senciente.alterego})

        if self.__viloes is not None:
            self.__tela_senciente.mostra_mensagem("----- Lista de Vilões -----")
            for senciente in self.__viloes:
                self.__tela_senciente.mostra_senciente({'codigo': 2,
                                                        'nome': senciente.nome,
                                                        'fraqueza': senciente.fraqueza,
                                                        'empresa': senciente.empresa,
                                                        'local_moradia': senciente.local_moradia,
                                                        'periculosidade': senciente.periculosidade})

    def excluir_senciente(self):
        if self.__viloes == [] and self.__super_herois == []:
            self.__tela_senciente.mostra_mensagem("\033[1;31mATENÇÃO: Ainda não há sencientes cadastrados.\033[0m")
            print()
            self.abre_tela()
        self.listar_senciente()
        nome_senciente = self.__tela_senciente.seleciona_senciente()
        senciente = self.pega_senciente_por_nome(nome_senciente)

        if senciente is not None:
            if isinstance(senciente, SuperHeroi):
                self.__super_herois.remove(senciente)
                # del(senciente) deleta o objeto da memória de vez
            elif isinstance(senciente, Vilao):
                self.__viloes.remove(senciente)
            self.listar_senciente()
        else:
            self.__tela_senciente.mostra_mensagem("Atenção: senciente não existente!")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def checar_lista_super_herois(self):
        if len(self.__super_herois) == 0:
            return 0

    def inclui_poder_em_senciente(self):
        poder = self.__controlador_sistema.controlador_poder.inclui_poder()
        return poder

    def abre_tela(self):
        lista_opcoes = {"Novo Super-Herói": self.incluir_super_heroi, "Novo Vilão": self.incluir_vilao,
                        "Alterar": self.alterar_senciente, # 3: self.listar_senciente,
                        "Excluir": self.excluir_senciente, # 0: self.retornar
                        }

        continua = True
        while continua:
            dict_super_herois = self.monta_dict_super_herois()
            dict_viloes = self.monta_dict_viloes()
            button, values = self.__tela_senciente_gui.open([dict_super_herois, dict_viloes])
            print(button)
            print(values)
            lista_opcoes[button](values)

            # lista_opcoes[self.__tela_senciente_gui.open()]()
