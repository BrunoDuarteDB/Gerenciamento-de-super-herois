from MVC.entidade.poder import Poder
from MVC.limite.tela_poder_gui import TelaPoderGUI
from MVC.limite.tela_dados_poder import TelaDadosPoder
from MVC.persistencia.poder_dao import PoderDAO


class ControladorPoder:
    def __init__(self, controlador_sistema):
        self.__tela_poder_gui = TelaPoderGUI(self)
        self.__tela_dados_poder = TelaDadosPoder(self)
        self.__controlador_sistema = controlador_sistema
        self.__poder_dao = PoderDAO()

    @property
    def poderes(self):
        return self.__poder_dao.get_all()

    def inclui_poder(self, nome):
        while True:
            if isinstance(nome, str):
                button, values = self.__tela_dados_poder.open(nome)
            elif isinstance(nome, dict):
                button, values = self.__tela_dados_poder.open(
                    dados_poder={"detentor": "", "inteligencia": "", "velocidade": "", "artes_marciais": "",
                                 "forca": "", "fator_cura": "", "poder_magico": "", "expertise": "",
                                 "resistencia": "", "controle_natureza": ""})
            self.__tela_dados_poder.close()

            try:
                int(values["velocidade"])
                int(values["forca"])
                int(values["poder_magico"])
                int(values["resistencia"])
                int(values["inteligencia"])
                int(values["artes_marciais"])
                int(values["fator_cura"])
                int(values["expertise"])
                int(values["controle_natureza"])
                if values == {'detentor': '', 'inteligencia': '', 'velocidade': '', 'artes_marciais': '', 'forca': '',
                              'fator_cura': '', 'poder_magico': '', 'expertise': '', 'resistencia': '',
                              'controle_natureza': ''} or \
                        (values['detentor'].isdigit()) == True:
                    raise ValueError
                media_poder = (int(values["velocidade"]) + int(values["forca"]) + int(values["poder_magico"]) +
                               int(values["resistencia"]) + int(values["inteligencia"]) + int(
                            values["artes_marciais"]) +
                               int(values["fator_cura"]) + int(values["expertise"]) + int(
                            values["controle_natureza"])) / 9

                poder = Poder(values["velocidade"], values["forca"], values["poder_magico"],
                              values["resistencia"], values["inteligencia"], values["artes_marciais"],
                              values["fator_cura"], values["expertise"], values["controle_natureza"],
                              values["detentor"], media_poder)
                self.__poder_dao.persist(poder)
                self.__tela_dados_poder.close()
                self.__tela_poder_gui.close()
                return poder
            except ValueError:
                self.__tela_poder_gui.show_message('Atenção', 'Valores inválidos, tente novamente!')
                continue

    def monta_dict_poderes(self):
        poderes = []
        for poder in self.__poder_dao.get_all():
            poderes.append(poder.detentor)
        return poderes

    def altera_poder(self, dados_poder):

        if self.__poder_dao.get_all() == []: #Mudar!!!!!!!!!!!!!!!!!!!!!!!!
            self.__tela_poder_gui.show_message("Atenção!", "Ainda não há clientes cadastrados.")

        detentor_poder_alterado = dados_poder['lb_itens'][0]

        lista_poderes = self.__poder_dao.get_all()

        for poder in lista_poderes:
            if poder.detentor == detentor_poder_alterado:
                dados_poder = {"detentor": poder.detentor, "inteligencia": poder.inteligencia,
                               "velocidade": poder.velocidade,
                               "artes_marciais": poder.artes_marciais, "forca": poder.forca,
                               "fator_cura": poder.fator_cura, "poder_magico": poder.poder_magico,
                               "expertise": poder.expertise, "resistencia": poder.resistencia,
                               "controle_natureza": poder.controle_natureza}

        while True:
            try:
                button, values = self.__tela_dados_poder.open(dados_poder)
                self.__tela_dados_poder.close()
                values["velocidade"] = int(values["velocidade"])
                values["forca"] = int(values["forca"])
                values["poder_magico"] = int(values["poder_magico"])
                values["resistencia"] = int(values["resistencia"])
                values["inteligencia"] = int(values["inteligencia"])
                values["artes_marciais"] = int(values["artes_marciais"])
                values["fator_cura"] = int(values["fator_cura"])
                values["expertise"] = int(values["expertise"])
                values["controle_natureza"] = int(values["controle_natureza"])
                if values == {'detentor': '', 'inteligencia': '', 'velocidade': '', 'artes_marciais': '', 'forca': '',
                              'fator_cura': '', 'poder_magico': '', 'expertise': '', 'resistencia': '',
                              'controle_natureza': ''} or \
                        (values['detentor'].isdigit()) == True:
                    raise ValueError
                lista_poderes = self.__poder_dao.get_all()

                for poder in lista_poderes:
                    if poder.detentor == detentor_poder_alterado:

                        poder.detentor = values["detentor"]
                        poder.inteligencia = values["inteligencia"]
                        poder.velocidade = values["velocidade"]
                        poder.artes_marciais = values["artes_marciais"]
                        poder.forca = values["forca"]
                        poder.fator_cura = values["fator_cura"]
                        poder.poder_magico = values["poder_magico"]
                        poder.expertise = values["expertise"]
                        poder.resistencia = values["resistencia"]
                        poder.controle_natureza = values["controle_natureza"]

                        self.__poder_dao.persist(poder)
                break
            except ValueError:
                self.__tela_poder_gui.show_message('Atenção', 'Valores inválidos, tente novamente!')
                continue

        self.__tela_dados_poder.close()
        self.__tela_poder_gui.close()

    def exclui_poder(self, dados_poder):
        if self.__poder_dao.get_all() == []:
            self.__tela_poder_gui.show_message("Atenção!", "Ainda não há poderes cadastrados.")
        detentor_poder_excluido = dados_poder['lb_itens'][0]
        poder_excluido = ''
        for poder in self.__poder_dao.get_all():
            if poder.detentor == detentor_poder_excluido:
                poder_excluido = poder
        self.__poder_dao.remove(poder_excluido)
        del poder_excluido
        self.__tela_poder_gui.close()

    def exclui_poder_de_senciente(self, poder_excluido):
        self.__poder_dao.remove(poder_excluido)
        del poder_excluido

    def inclui_poder_em_senciente(self, dados_poder):
        if self.__poder_dao.get_all() == []:
            self.__tela_poder_gui.show_message("Atenção!", "Ainda não há poderes cadastrados.")
        detentor_poder_incluido = dados_poder['lb_itens'][0]
        for poder in self.__poder_dao.get_all():
            if poder.detentor == detentor_poder_incluido:
                dados_poder = {"detentor": poder.detentor, "inteligencia": poder.inteligencia,
                               "velocidade": poder.velocidade,
                               "artes_marciais": poder.artes_marciais, "forca": poder.forca,
                               "fator_cura": poder.fator_cura, "poder_magico": poder.poder_magico,
                               "expertise": poder.expertise, "resistencia": poder.resistencia,
                               "controle_natureza": poder.controle_natureza}
        self.__tela_poder_gui.close()

    def retornar(self, values):
        self.__tela_poder_gui.close()
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            "Incluir": self.inclui_poder,
            "Alterar": self.altera_poder,
            "Excluir": self.exclui_poder,
            "Retornar": self.retornar,
            "Incluir em Senciente": self.inclui_poder_em_senciente
        }
        continua = True
        while continua:
            dict_poderes = self.monta_dict_poderes()
            button, values = self.__tela_poder_gui.open(dict_poderes)
            lista_opcoes[button](values)

            # lista_opcoes[self.__tela_poder_gui.open()]()
