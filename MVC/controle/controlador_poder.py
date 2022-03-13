from MVC.entidade.poder import Poder
from MVC.limite.tela_poder import TelaPoder
from MVC.limite.tela_poder_gui import TelaPoderGUI
from MVC.limite.tela_dados_poder import TelaDadosPoder


class ControladorPoder:
    def __init__(self, controlador_sistema):
        self.__poderes = []
        self.__tela_poder_gui = TelaPoderGUI(self)
        self.__tela_dados_poder = TelaDadosPoder(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def poderes(self):
        return self.__poderes

    def pega_poder_por_detentor(self, detentor: str):
        for poder in self.__poderes:
            if poder.detentor == detentor:
                return poder
        return None

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
                self.__poderes.append(poder)
                self.__tela_dados_poder.close()
                self.__tela_poder_gui.close()
                return poder
            except ValueError:
                self.__tela_poder_gui.show_message('Atenção', 'Valores inválidos, tente novamente!')
                continue

        '''
        if nome is not None:
            dados_poder = self.__tela_poder.pega_dados_poder(nome)
        elif nome is None:
            dados_poder = self.__tela_poder.pega_dados_poder()

        media_poder = (dados_poder["velocidade"] + dados_poder["forca"] + dados_poder["poder_magico"] +
                       dados_poder["resistencia"] + dados_poder["inteligencia"] + dados_poder["artes_marciais"] +
                       dados_poder["fator_cura"] + dados_poder["expertise"] + dados_poder["controle_natureza"]) / 9
        poder = Poder(dados_poder["velocidade"], dados_poder["forca"], dados_poder["poder_magico"],
                      dados_poder["resistencia"], dados_poder["inteligencia"], dados_poder["artes_marciais"],
                      dados_poder["fator_cura"], dados_poder["expertise"], dados_poder["controle_natureza"],
                      dados_poder["detentor"], media_poder)
        self.__poderes.append(poder)
        return poder'''

    def monta_dict_poderes(self):
        poderes = []
        for poder in self.__poderes:
            poderes.append(poder.detentor)
        return poderes

    def altera_poder(self, dados_poder):

        if self.__poderes == []:
            self.__tela_poder_gui.show_message("Atenção!", "Ainda não há clientes cadastrados.")

        detentor_poder_alterado = dados_poder['lb_itens'][0]

        for poder in self.__poderes:
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
                for poder in self.__poderes:
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
                break
            except ValueError:
                self.__tela_poder_gui.show_message('Atenção', 'Valores inválidos, tente novamente!')
                continue

        self.__tela_dados_poder.close()
        self.__tela_poder_gui.close()

        '''if self.__poderes == []:
            self.__tela_poder.mostra_mensagem("\033[1;31mATENÇÃO: Ainda não há poderes cadastrados.\033[0m")
            print()
            self.abre_tela()
        self.lista_poderes()
        detentor_do_poder = self.__tela_poder.seleciona_poder()
        poder = self.pega_poder_por_detentor(detentor_do_poder)

        if poder is not None:
            novos_dados_poder = self.__tela_poder.pega_dados_poder()
            poder.velocidade = novos_dados_poder["velocidade"]
            poder.forca = novos_dados_poder["forca"]
            poder.poder_magico = novos_dados_poder["poder_magico"]
            poder.resistencia = novos_dados_poder["resistencia"]
            poder.inteligencia = novos_dados_poder["inteligencia"]
            poder.artes_marciais = novos_dados_poder["artes_marciais"]
            poder.fator_cura = novos_dados_poder["fator_cura"]
            poder.expertise = novos_dados_poder["expertise"]
            poder.controle_natureza = novos_dados_poder["controle_natureza"]
            poder.detentor = novos_dados_poder["detentor"]
            self.lista_poderes()
        else:
            self.__tela_poder.mostra_mensagem("\033[1;31mATENÇÃO! PODER INEXISTENTE \033[0m")'''

    def lista_poderes(self):
        if len(self.__poderes) == 0:
            self.__tela_poder.mostra_mensagem("\033[1;31mA LISTA DE PODERES ESTÁ VAZIA. \033[0m")
        elif len(self.__poderes) > 0:
            self.__tela_poder.mostra_mensagem("----- Lista de Poderes -----")
        for poder in self.__poderes:
            self.__tela_poder.mostra_poder({"detentor": poder.detentor, "velocidade": poder.velocidade,
                                            "forca": poder.forca, "poder_magico": poder.poder_magico,
                                            "resistencia": poder.resistencia, "inteligencia": poder.inteligencia,
                                            "artes_marciais": poder.artes_marciais, "fator_cura": poder.fator_cura,
                                            "expertise": poder.expertise, "controle_natureza": poder.controle_natureza})

    def exclui_poder(self, dados_poder):
        if self.__poderes == []:
            self.__tela_poder_gui.show_message("Atenção!", "Ainda não há poderes cadastrados.")

        detentor_poder_excluido = dados_poder['lb_itens'][0]

        for poder in self.__poderes:
            if poder.detentor == detentor_poder_excluido:
                self.__poderes.remove(poder)
                del poder

        self.__tela_poder_gui.close()

    def inclui_poder_em_senciente(self, dados_poder):
        if self.__poderes == []:
            self.__tela_poder_gui.show_message("Atenção!", "Ainda não há poderes cadastrados.")
        detentor_poder_incluido = dados_poder['lb_itens'][0]
        for poder in self.__poderes:
            if poder.detentor == detentor_poder_incluido:
                dados_poder = {"detentor": poder.detentor, "inteligencia": poder.inteligencia,
                               "velocidade": poder.velocidade,
                               "artes_marciais": poder.artes_marciais, "forca": poder.forca,
                               "fator_cura": poder.fator_cura, "poder_magico": poder.poder_magico,
                               "expertise": poder.expertise, "resistencia": poder.resistencia,
                               "controle_natureza": poder.controle_natureza}
        self.__tela_poder_gui.close()

        '''if self.__poderes == []:
            self.__tela_poder.mostra_mensagem("\033[1;31mATENÇÃO: Ainda não há poderes cadastrados.\033[0m")
            print()
            self.abre_tela()
        self.lista_poderes()
        detentor_do_poder = self.__tela_poder.seleciona_poder()

        for i in self.__controlador_sistema.controlador_senciente.super_herois:
            if i.nome == detentor_do_poder:
                return self.__tela_poder.mostra_mensagem('\033[1;31mEste poder não pode ser excluído '
                                                         'pois pertence a um Super-Herói!\033[0m')

        for j in self.__controlador_sistema.controlador_senciente.viloes:
            if j.nome == detentor_do_poder:
                return self.__tela_poder.mostra_mensagem('\033[1;31mEste poder não pode ser excluído '
                                                         'pois pertence a um Vilão!\033[0m')

        poder = self.pega_poder_por_detentor(detentor_do_poder)

        if poder is not None:
            self.__poderes.remove(poder)
            self.lista_poderes()
        else:
            self.__tela_poder.mostra_mensagem("ATENÇÃO: Poder não existente.")'''

    def mostra_media_poder(self):
        detentor_do_poder = self.__tela_poder.seleciona_poder()
        poder = self.pega_poder_por_detentor(detentor_do_poder)
        if poder is not None:
            media = (poder.velocidade + poder.forca + poder.poder_magico + poder.resistencia + poder.inteligencia +
                     poder.artes_marciais + poder.fator_cura + poder.expertise + poder.controle_natureza) / 9
            return self.__tela_poder.mostra_mensagem(
                f"\033[1;33mA média de poder do detentor escolhido é: {media}\033[0m ")
        else:
            return self.__tela_poder.mostra_mensagem(
                "\033[1;31mDETENTOR DO PODER INVÁLIDO. VERIFIQUE SE DIGITOU CORRETAMENTE \033[0m")

    def retornar(self, values):
        self.__tela_poder_gui.close()
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            "Incluir": self.inclui_poder,
            "Alterar": self.altera_poder,
            # 3: self.lista_poderes,
            "Excluir": self.exclui_poder,
            # 5: self.mostra_media_poder,
            "Retornar": self.retornar,
            "Incluir em Senciente": self.inclui_poder_em_senciente
        }
        continua = True
        while continua:
            dict_poderes = self.monta_dict_poderes()
            button, values = self.__tela_poder_gui.open(dict_poderes)
            lista_opcoes[button](values)

            # lista_opcoes[self.__tela_poder_gui.open()]()
