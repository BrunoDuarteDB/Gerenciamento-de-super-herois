from MVC.entidade.super_heroi import SuperHeroi
from MVC.entidade.vilao import Vilao
from MVC.limite.tela_senciente_gui import TelaSencienteGUI
from MVC.limite.tela_dados_super_heroi import TelaDadosSuperHeroi
from MVC.limite.tela_dados_vilao import TelaDadosVilao
from MVC.persistencia.super_heroi_dao import SuperHeroiDAO
from MVC.persistencia.vilao_dao import VilaoDAO


class ControladorSenciente:

    def __init__(self, controlador_sistema):
        self.__tela_senciente_gui = TelaSencienteGUI(self)
        self.__tela_dados_super_heroi = TelaDadosSuperHeroi(self)
        self.__tela_dados_vilao = TelaDadosVilao(self)
        self.__controlador_sistema = controlador_sistema
        self.__super_heroi_dao = SuperHeroiDAO()
        self.__vilao_dao = VilaoDAO()

    @property
    def super_herois(self):
        return self.__super_heroi_dao.get_all()

    @property
    def viloes(self):
        return self.__vilao_dao.get_all()

    def pede_cadastro_poder(self, nome):
        poder = self.__controlador_sistema.controlador_poder.inclui_poder(nome)
        return poder

    def incluir_super_heroi(self, values):
        while True:
            button, values = self.__tela_dados_super_heroi.open()

            try:
                if values['nome'] == '' or values['fraqueza'] == '' or values['empresa'] == '' or values['local_moradia']== '' \
                            or values['alterego']== '' or (values['nome']).isdigit() == True or (values['fraqueza']).isdigit() == True \
                        or (values['empresa']).isdigit() == True or (values['local_moradia']).isdigit() == True or \
                        (values['alterego']).isdigit() == True:
                    raise ValueError
                poder = self.__controlador_sistema.controlador_poder.inclui_poder(values['nome'])
                senciente = SuperHeroi(values['nome'], poder, values['fraqueza'],
                                       values['empresa'], values['local_moradia'],
                                       values['alterego'])
                self.__super_heroi_dao.persist(senciente)
                self.__tela_dados_super_heroi.close()
                self.__tela_senciente_gui.close()
                break
            except ValueError:
                self.__tela_senciente_gui.show_message('Atenção!', 'Valores inválidos, tente novamente!')
                continue

    def incluir_vilao(self, values):
        while True:
            button, values = self.__tela_dados_vilao.open()
            try:
                values['periculosidade']= int(values['periculosidade'])
                if values['nome'] == '' or values['fraqueza'] == '' or values['empresa'] == '' or values['local_moradia']== '' \
                            or values['periculosidade']== '' or (values['nome']).isdigit() == True or (values['fraqueza']).isdigit() == True \
                        or (values['empresa']).isdigit() == True or (values['local_moradia']).isdigit() == True:
                    raise ValueError
                poder = self.__controlador_sistema.controlador_poder.inclui_poder(values['nome'])
                senciente = Vilao(values['nome'], poder, values['fraqueza'],
                                       values['empresa'], values['local_moradia'],
                                       values['periculosidade'])
                self.__vilao_dao.persist(senciente)
                self.__tela_dados_vilao.close()
                self.__tela_senciente_gui.close()
                break
            except ValueError:
                self.__tela_senciente_gui.show_message('Atenção!', 'Valores inválidos, tente novamente!')
                continue

    def monta_dict_super_herois(self):
        super_herois = []
        for super_heroi in self.__super_heroi_dao.get_all():
            super_herois.append(super_heroi.nome)
        return super_herois

    def monta_dict_viloes(self):
        viloes = []
        for vilao in self.__vilao_dao.get_all():
            viloes.append(vilao.nome)
        return viloes

    def seleciona_senciente(self):
        sencientes = []
        dict_super_herois = self.monta_dict_super_herois()
        dict_viloes = self.monta_dict_viloes()
        button = 'Incluir mais Sencientes'
        while button == 'Incluir mais Sencientes':
            button, values = self.__tela_senciente_gui.open([dict_super_herois, dict_viloes])
            self.__tela_senciente_gui.close()
            if values['lb_itens'] != []:
                sencientes.append(values['lb_itens'])
            if values['lb_itens0'] != []:
                sencientes.append(values['lb_itens0'])
        return sencientes

    def alterar_senciente(self, dados_senciente):
        if self.__super_heroi_dao.get_all() == [] and self.__vilao_dao.get_all() == []:
            self.__tela_senciente_gui.show_message("Atenção!", "Ainda não há sencientes cadastrados.")

        if dados_senciente['lb_itens'] != []:
            nome_super_alterado = dados_senciente['lb_itens'][0]
            for super_heroi in self.__super_heroi_dao.get_all():
                if super_heroi.nome == nome_super_alterado:
                    dados_senciente = {"nome": super_heroi.nome, "fraqueza": super_heroi.fraqueza,
                                       "empresa": super_heroi.empresa,
                                       "local_moradia": super_heroi.local_moradia, "alterego": super_heroi.alterego}
                while True:
                    try:
                        button, values = self.__tela_dados_super_heroi.open(dados_senciente)
                        if values['nome'] == '' or values['fraqueza'] == '' or values['empresa'] == '' or values[
                            'local_moradia'] == '' \
                                or values['alterego'] == '' or (values['nome']).isdigit() == True or (
                                values['fraqueza']).isdigit() == True \
                                or (values['empresa']).isdigit() == True or (values['local_moradia']).isdigit() == True or \
                                (values['alterego']).isdigit() == True:
                            raise ValueError
                        for super_heroi in self.__super_heroi_dao.get_all():
                            if super_heroi.nome == nome_super_alterado:
                                super_heroi.nome = values["nome"]
                                super_heroi.fraqueza = values["fraqueza"]
                                super_heroi.empresa = values["empresa"]
                                super_heroi.local_moradia = values["local_moradia"]
                                super_heroi.alterego = values["alterego"]
                                self.__super_heroi_dao.persist(super_heroi)
                        break
                    except ValueError:
                        self.__tela_senciente_gui.show_message('Atenção', 'Valores inválidos, tente novamente!')
                        continue

                self.__tela_dados_super_heroi.close()
                self.__tela_senciente_gui.close()

        elif dados_senciente['lb_itens0'] != []:
            nome_vilao_alterado = dados_senciente['lb_itens0'][0]
            for vilao in self.__vilao_dao.get_all():
                if vilao.nome == nome_vilao_alterado:
                    dados_senciente = {"nome": vilao.nome, "fraqueza": vilao.fraqueza,
                                       "empresa": vilao.empresa,
                                       "local_moradia": vilao.local_moradia, "periculosidade": vilao.periculosidade}
            while True:
                try:
                    button, values = self.__tela_dados_vilao.open(dados_senciente)
                    (values['periculosidade'])= int(values['periculosidade'])
                    if values['nome'] == '' or values['fraqueza'] == '' or values['empresa'] == '' or values[
                        'local_moradia'] == '' or values['periculosidade'] == '' or (values['nome']).isdigit() == True or\
                            (values['fraqueza']).isdigit() == True or (values['empresa']).isdigit() == True or\
                            (values['local_moradia']).isdigit() == True:
                        raise ValueError
                    for vilao in self.__vilao_dao.get_all():
                        if vilao.nome == nome_vilao_alterado:
                            vilao.nome = values["nome"]
                            vilao.fraqueza = values["fraqueza"]
                            vilao.empresa = values["empresa"]
                            vilao.local_moradia = values["local_moradia"]
                            vilao.periculosidade = values["periculosidade"]
                            self.__vilao_dao.persist(vilao)
                    break
                except ValueError:
                    self.__tela_senciente_gui.show_message('Atenção', 'Valores inválidos, tente novamente!')
                    continue

            self.__tela_dados_vilao.close()
            self.__tela_senciente_gui.close()

    def excluir_senciente(self, dados_senciente):
        if self.__super_heroi_dao.get_all() == [] and self.__vilao_dao.get_all() == []:
            self.__tela_senciente_gui.show_message("Atenção!", "Ainda não há sencientes cadastrados.")

        if dados_senciente['lb_itens'] != []:
            nome_super_excluido = dados_senciente['lb_itens'][0]

            lista_poderes = self.__controlador_sistema.controlador_poder.poder_dao.get_all()
            poder_excluido = ''
            for poder in lista_poderes:
                if poder.detentor == nome_super_excluido:
                    poder_excluido = poder
            self.__controlador_sistema.controlador_poder.poder_dao.remove(poder_excluido)
            del poder_excluido

            lista_super_herois = self.__super_heroi_dao.get_all()
            super_heroi_excluido = ''
            for super_heroi in lista_super_herois:
                if super_heroi.nome == nome_super_excluido:
                    super_heroi_excluido = super_heroi
            self.__super_heroi_dao.remove(super_heroi_excluido)
            del super_heroi_excluido

        elif dados_senciente['lb_itens0'] != []:
            nome_vilao_excluido = dados_senciente['lb_itens0'][0]

            lista_poderes = self.__controlador_sistema.controlador_poder.poder_dao.get_all()
            poder_excluido = ''
            for poder in lista_poderes:
                if poder.detentor == nome_vilao_excluido:
                    poder_excluido = poder
            self.__controlador_sistema.controlador_poder.poder_dao.remove(poder_excluido)
            del poder_excluido

            lista_viloes = self.__vilao_dao.get_all()
            vilao_excluido = ''
            for vilao in lista_viloes:
                if vilao.nome == nome_vilao_excluido:
                    vilao_excluido = vilao
            self.__vilao_dao.remove(vilao_excluido)
            del vilao_excluido

        self.__tela_senciente_gui.close()

    def retornar(self, values):
        self.__tela_senciente_gui.close()
        self.__controlador_sistema.abre_tela()

    def checar_lista_super_herois(self):
        super_herois = []
        for super_heroi in self.__super_heroi_dao.get_all():
            super_herois.append(super_heroi)
        if super_herois == []:
            return 0

    def inclui_poder_em_senciente(self):
        poder = self.__controlador_sistema.controlador_poder.inclui_poder()
        return poder

    def abre_tela(self):
        lista_opcoes = {"Novo Super-Herói": self.incluir_super_heroi, "Novo Vilão": self.incluir_vilao,
                        "Alterar": self.alterar_senciente,  "Excluir": self.excluir_senciente, "Retornar": self.retornar
                        }

        continua = True
        while continua:
            dict_super_herois = self.monta_dict_super_herois()
            dict_viloes = self.monta_dict_viloes()
            button, values = self.__tela_senciente_gui.open([dict_super_herois, dict_viloes])
            lista_opcoes[button](values)

            # lista_opcoes[self.__tela_senciente_gui.open()]()
