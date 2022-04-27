from MVC.entidade.super_heroi import SuperHeroi
from MVC.entidade.vilao import Vilao
from MVC.limite.tela_senciente_gui import TelaSencienteGUI
from MVC.limite.tela_dados_super_heroi import TelaDadosSuperHeroi
from MVC.limite.tela_dados_vilao import TelaDadosVilao
from MVC.persistencia.super_heroi_dao import SuperHeroiDAO
from MVC.persistencia.vilao_dao import VilaoDAO
from MVC.exceptions.botaoErradoException import BotaoErradoException
from MVC.exceptions.listaVaziaException import ListaVaziaException
from MVC.exceptions.nadaSelecionadoException import NadaSelecionadoException
from MVC.exceptions.jaExistenteException import JaExistenteException


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
                if values['nome'] == '' or values['fraqueza'] == '' or values['empresa'] == '' or values[
                    'local_moradia'] == '' \
                        or values['alterego'] == '' or (values['nome']).isdigit() == True or (
                        values['fraqueza']).isdigit() == True \
                        or (values['empresa']).isdigit() == True or (values['local_moradia']).isdigit() == True or \
                        (values['alterego']).isdigit() == True:
                    raise ValueError

                for super_heroi in self.__super_heroi_dao.get_all():
                    if super_heroi.nome == values['nome']:
                        raise JaExistenteException

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
            except JaExistenteException:
                self.__tela_senciente_gui.show_message('Atenção', 'Super-Herói já existente, tente novamente!')
                continue

    def incluir_vilao(self, values):
        while True:
            button, values = self.__tela_dados_vilao.open()
            try:
                values['periculosidade'] = int(values['periculosidade'])
                if values['nome'] == '' or values['fraqueza'] == '' or values['empresa'] == '' or values[
                    'local_moradia'] == '' \
                        or values['periculosidade'] == '' or (values['nome']).isdigit() == True or (
                        values['fraqueza']).isdigit() == True \
                        or (values['empresa']).isdigit() == True or (values['local_moradia']).isdigit() == True:
                    raise ValueError

                for vilao in self.__vilao_dao.get_all():
                    if vilao.nome == values['nome']:
                        raise JaExistenteException

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
            except JaExistenteException:
                self.__tela_senciente_gui.show_message('Atenção', 'Vilão já existente, tente novamente!')
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

            while True:
                button, values = self.__tela_senciente_gui.open([dict_super_herois, dict_viloes])

                try:
                    if button != 'Incluir mais Sencientes' and button != 'Incluir em Missão':
                        raise BotaoErradoException
                    break
                except BotaoErradoException:
                    self.__tela_senciente_gui.show_message('Ops',
                                                           'Você deve clicar em "Incluir mais Sencientes" ou "Incluir'
                                                           'em Missão"!')
                    self.__tela_senciente_gui.close()
                    continue

            self.__tela_senciente_gui.close()
            if values['lb_itens'] != []:
                sencientes.append(values['lb_itens'])
            if values['lb_itens0'] != []:
                sencientes.append(values['lb_itens0'])
        return sencientes

    def alterar_senciente(self, dados_senciente):
        try:
            checagem_super = self.checar_lista_super_herois()
            checagem_vilao = self.checar_lista_viloes()
            if checagem_super == 0 and checagem_vilao == 0:
                raise ListaVaziaException
            if dados_senciente['lb_itens'] == [] and dados_senciente['lb_itens0'] == []:
                raise NadaSelecionadoException
            else:
                if dados_senciente['lb_itens'] != []:
                    nome_super_alterado = dados_senciente['lb_itens'][0]
                    for super_heroi in self.__super_heroi_dao.get_all():
                        if super_heroi.nome == nome_super_alterado:
                            dados_senciente = {"nome": super_heroi.nome, "fraqueza": super_heroi.fraqueza,
                                               "empresa": super_heroi.empresa,
                                               "local_moradia": super_heroi.local_moradia,
                                               "alterego": super_heroi.alterego}
                    while True:
                        try:
                            button, values = self.__tela_dados_super_heroi.open(dados_senciente)
                            self.__tela_dados_super_heroi.close()
                            if values['nome'] == '' or values['fraqueza'] == '' or values['empresa'] == '' or values[
                                'local_moradia'] == '' \
                                    or values['alterego'] == '' or (values['nome']).isdigit() == True or (
                                    values['fraqueza']).isdigit() == True \
                                    or (values['empresa']).isdigit() == True or (
                                    values['local_moradia']).isdigit() == True or \
                                    (values['alterego']).isdigit() == True:
                                raise ValueError

                            for super_heroi in self.__super_heroi_dao.get_all():
                                if super_heroi.nome == values['nome'] and super_heroi.nome != \
                                        dados_senciente['nome']:
                                    raise JaExistenteException

                            for super_heroi in self.__super_heroi_dao.get_all():
                                if super_heroi.nome == nome_super_alterado:
                                    super_desejado = super_heroi
                                    poder_do_super = super_heroi.poder

                            if values['nome'] != nome_super_alterado:
                                self.__super_heroi_dao.remove(super_desejado)
                                super_heroi = SuperHeroi(values["nome"], poder_do_super, values["fraqueza"],
                                                         values["empresa"], values["local_moradia"], values["alterego"])
                                self.__super_heroi_dao.persist(super_heroi)
                                self.__tela_senciente_gui.close()

                            elif values['nome'] == nome_super_alterado:
                                super_desejado.fraqueza = values['fraqueza']
                                super_desejado.empresa = values['empresa']
                                super_desejado.local_moradia = values['local_moradia']
                                super_desejado.alterego = values['alterego']

                            break

                        except ValueError:
                            self.__tela_senciente_gui.show_message('Atenção', 'Valor(es) inválido(s), tente novamente!')
                            continue
                        except JaExistenteException:
                            self.__tela_senciente_gui.show_message('Atenção',
                                                                   'Super-herói já existente, tente novamente!')
                            continue

                    self.__tela_dados_super_heroi.close()
                    self.__tela_senciente_gui.close()

                elif dados_senciente['lb_itens0'] != []:
                    nome_vilao_alterado = dados_senciente['lb_itens0'][0]
                    for vilao in self.__vilao_dao.get_all():
                        if vilao.nome == nome_vilao_alterado:
                            dados_senciente = {"nome": vilao.nome, "fraqueza": vilao.fraqueza,
                                               "empresa": vilao.empresa,
                                               "local_moradia": vilao.local_moradia,
                                               "periculosidade": vilao.periculosidade}

                    while True:
                        try:
                            button, values = self.__tela_dados_vilao.open(dados_senciente)
                            values['periculosidade'] = int(values['periculosidade'])
                            if values['nome'] == '' or values['fraqueza'] == '' or values['empresa'] == '' or values[
                                'local_moradia'] == '' or values['periculosidade'] == '' or (
                                    values['nome']).isdigit() == True or \
                                    (values['fraqueza']).isdigit() == True or (values['empresa']).isdigit() == True or \
                                    (values['local_moradia']).isdigit() == True:
                                raise ValueError

                            for vilao in self.__vilao_dao.get_all():
                                if vilao.nome == values['nome'] and vilao.nome != \
                                        dados_senciente['nome']:
                                    raise JaExistenteException

                            for vilao in self.__vilao_dao.get_all():
                                if vilao.nome == nome_vilao_alterado:
                                    vilao_desejado = vilao
                                    poder_do_vilao = vilao.poder

                            if values['nome'] != nome_vilao_alterado:
                                self.__vilao_dao.remove(vilao_desejado)
                                vilao = Vilao(values["nome"], poder_do_vilao, values["fraqueza"],
                                              values["empresa"], values["local_moradia"], values["periculosidade"])
                                self.__vilao_dao.persist(vilao)
                                self.__tela_senciente_gui.close()

                            elif values['nome'] == nome_vilao_alterado:
                                vilao_desejado.fraqueza = values['fraqueza']
                                vilao_desejado.empresa = values['empresa']
                                vilao_desejado.local_moradia = values['local_moradia']
                                vilao_desejado.periculosidade = values['periculosidade']

                            break

                        except ValueError:
                            self.__tela_senciente_gui.show_message('Atenção', 'Valores inválidos, tente novamente!')
                            continue
                        except JaExistenteException:
                            self.__tela_senciente_gui.show_message('Atenção', 'Vilão já existente, tente novamente!')
                            continue

                    self.__tela_dados_vilao.close()
                    self.__tela_senciente_gui.close()
        except NadaSelecionadoException:
            self.__tela_senciente_gui.show_message("Ops!", "Nenhum senciente foi selecionado.")
            self.__tela_senciente_gui.close()
        except ListaVaziaException:
            self.__tela_senciente_gui.show_message("Ops!", "Não há sencientes cadastrados.")
            self.__tela_senciente_gui.close()

    def excluir_senciente(self, dados_senciente):
        try:
            checagem_super = self.checar_lista_super_herois()
            checagem_vilao = self.checar_lista_viloes()
            if checagem_super == 0 and checagem_vilao == 0:
                raise ListaVaziaException
            if dados_senciente['lb_itens'] == [] and dados_senciente['lb_itens0'] == []:
                raise NadaSelecionadoException
            else:
                if dados_senciente['lb_itens'] != []:
                    nome_super_excluido = dados_senciente['lb_itens'][0]

                    lista_poderes = self.__controlador_sistema.controlador_poder.poderes
                    poder_excluido = ''
                    for poder in lista_poderes:
                        if poder.detentor == nome_super_excluido:
                            poder_excluido = poder
                    self.__controlador_sistema.controlador_poder.exclui_poder_de_senciente(poder_excluido)

                    lista_super_herois = self.__super_heroi_dao.get_all()
                    super_heroi_excluido = ''
                    for super_heroi in lista_super_herois:
                        if super_heroi.nome == nome_super_excluido:
                            super_heroi_excluido = super_heroi
                    self.__super_heroi_dao.remove(super_heroi_excluido)
                    del super_heroi_excluido

                elif dados_senciente['lb_itens0'] != []:
                    nome_vilao_excluido = dados_senciente['lb_itens0'][0]

                    lista_poderes = self.__controlador_sistema.controlador_poder.poderes
                    poder_excluido = ''
                    for poder in lista_poderes:
                        if poder.detentor == nome_vilao_excluido:
                            poder_excluido = poder
                    self.__controlador_sistema.controlador_poder.exclui_poder_de_senciente(poder_excluido)
                    del poder_excluido

                    lista_viloes = self.__vilao_dao.get_all()
                    vilao_excluido = ''
                    for vilao in lista_viloes:
                        if vilao.nome == nome_vilao_excluido:
                            vilao_excluido = vilao
                    self.__vilao_dao.remove(vilao_excluido)
                    del vilao_excluido

                self.__tela_senciente_gui.close()
        except NadaSelecionadoException:
            self.__tela_senciente_gui.show_message("Ops!", "Nenhum senciente foi selecionado.")
            self.__tela_senciente_gui.close()
        except ListaVaziaException:
            self.__tela_senciente_gui.show_message("Ops!", "Não há sencientes cadastrados.")
            self.__tela_senciente_gui.close()

    def mostrar_detalhes(self, values):
        try:
            checagem_super = self.checar_lista_super_herois()
            checagem_vilao = self.checar_lista_viloes()
            if checagem_super == 0 and checagem_vilao == 0:
                raise ListaVaziaException
            if values['lb_itens'] == [] and values['lb_itens0'] == []:
                raise NadaSelecionadoException
            else:
                nome_desejado = values['lb_itens'][0]

                for super_heroi in self.__super_heroi_dao.get_all():
                    if super_heroi.nome == nome_desejado:
                        fraqueza = super_heroi.fraqueza
                        empresa = super_heroi.empresa
                        local_moradia = super_heroi.local_moradia
                        alterego = super_heroi.alterego
                        self.__tela_senciente_gui.close()
                        self.__tela_senciente_gui.show_message("Detalhes do Senciente:",
                                                               f'Nome: {nome_desejado}, Fraqueza: {fraqueza},  Empresa: {empresa}, Local de moradia: {local_moradia}, Alter ego: {alterego}.')
        except NadaSelecionadoException:
            self.__tela_senciente_gui.show_message("Ops!", "Nenhum senciente foi selecionado.")
            self.__tela_senciente_gui.close()
        except ListaVaziaException:
            self.__tela_senciente_gui.show_message("Ops!", "Não há sencientes cadastrados.")
            self.__tela_senciente_gui.close()

        for vilao in self.__vilao_dao.get_all():
            if vilao.nome == nome_desejado:
                fraqueza = vilao.fraqueza
                empresa = vilao.empresa
                local_moradia = vilao.local_moradia
                periculosidade = vilao.periculosidade
                self.__tela_senciente_gui.close()
                self.__tela_senciente_gui.show_message("Detalhes do Senciente:",
                                                       f'Nome: {nome_desejado}, Fraqueza: {fraqueza},  Empresa: {empresa}, Local de moradia: {local_moradia}, Periculosidade: {periculosidade}.')

    def retornar(self, values):
        self.__tela_senciente_gui.close()
        self.__controlador_sistema.abre_tela()

    def checar_lista_super_herois(self):
        super_herois = []
        for super_heroi in self.__super_heroi_dao.get_all():
            super_herois.append(super_heroi)
        if super_herois == []:
            return 0

    def checar_lista_viloes(self):
        viloes = []
        for vilao in self.__vilao_dao.get_all():
            viloes.append(vilao)
        if viloes == []:
            return 0

    def inclui_poder_em_senciente(self):
        poder = self.__controlador_sistema.controlador_poder.inclui_poder()
        return poder

    def abre_tela(self):
        lista_opcoes = {"Novo Super-Herói": self.incluir_super_heroi, "Novo Vilão": self.incluir_vilao,
                        "Alterar": self.alterar_senciente, "Excluir": self.excluir_senciente,
                        "Mostrar Detalhes": self.mostrar_detalhes, "Retornar": self.retornar
                        }

        continua = True
        while continua:
            dict_super_herois = self.monta_dict_super_herois()
            dict_viloes = self.monta_dict_viloes()

            while True:
                button, values = self.__tela_senciente_gui.open([dict_super_herois, dict_viloes])

                try:
                    if button == 'Incluir mais Sencientes' or button == 'Incluir em Missão':
                        raise BotaoErradoException
                    break
                except BotaoErradoException:
                    self.__tela_senciente_gui.show_message('Ops!',
                                                           'Você só deve clicar nesse botão quando estiver cadastrando '
                                                           'uma missão!')
                    self.__tela_senciente_gui.close()
                    continue

            self.__tela_senciente_gui.close()
            lista_opcoes[button](values)

            # lista_opcoes[self.__tela_senciente_gui.open()]()
