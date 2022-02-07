from MVC.entidade.poder import Poder
from MVC.limite.tela_poder import TelaPoder

class ControladorPoder:
    def __init__(self, controlador_sistema):
        self.__poderes = []
        self.__tela_poder = TelaPoder(self)
        self.__controlador_sistema = controlador_sistema

    def pega_poder_por_detentor(self, detentor: str):
        for poder in self.__poderes:
            if (poder.detentor == detentor):
                return poder
        return None

    def inclui_poder(self):
        dados_poder = self.__tela_poder.pega_dados_poder()
        media_poder = (dados_poder["velocidade"] + dados_poder["forca"] + dados_poder["poder_magico"] +
                       dados_poder["resistencia"] + dados_poder["inteligencia"] + dados_poder["artes_marciais"] +
                       dados_poder["fator_cura"] + dados_poder["expertise"] + dados_poder["controle_natureza"]) / 9
        poder = Poder(dados_poder["velocidade"], dados_poder["forca"], dados_poder["poder_magico"],
                      dados_poder["resistencia"], dados_poder["inteligencia"], dados_poder["artes_marciais"],
                      dados_poder["fator_cura"], dados_poder["expertise"], dados_poder["controle_natureza"],
                      dados_poder["detentor"], media_poder)
        self.__poderes.append(poder)
        return poder

    def altera_poder(self):
        self.lista_poderes()
        detentor_do_poder = self.__tela_poder.seleciona_poder()
        poder = self.pega_poder_por_detentor(detentor_do_poder)

        if (poder is not None):
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
            self.__tela_poder.mostra_mensagem("\033[1;31mATENÇÃO! PODER INEXISTENTE \033[0m")

    def lista_poderes(self):
        if (len(self.__poderes) == 0):
            self.__tela_poder.mostra_mensagem("\033[1;31mA LISTA DE PODERES ESTÁ VAZIA. \033[0m")
        for poder in self.__poderes:
            self.__tela_poder.mostra_poder({"detentor": poder.detentor,"velocidade": poder.velocidade, "forca": poder.forca,
                                            "poder_magico": poder.poder_magico, "resistencia": poder.resistencia,
                                            "inteligencia": poder.inteligencia, "artes_marciais": poder.artes_marciais,
                                            "fator_cura": poder.fator_cura, "expertise": poder.expertise,
                                            "controle_natureza": poder.controle_natureza})

    def exclui_poder(self):
        self.lista_poderes()
        detentor_do_poder = self.__tela_poder.seleciona_poder()
        poder = self.pega_poder_por_detentor(detentor_do_poder)

        if (poder is not None):
            self.__poderes.remove(poder)
            self.lista_poderes()
        else:
            self.__tela_poder.mostra_mensagem("ATENÇÃO: Poder não existente.")

    def mostra_media_poder(self):
        detentor_do_poder = self.__tela_poder.seleciona_poder()
        poder = self.pega_poder_por_detentor(detentor_do_poder)
        if poder is not None:
            media = (poder.velocidade + poder.forca + poder.poder_magico + poder.resistencia + poder.inteligencia +
                 poder.artes_marciais + poder.fator_cura + poder.expertise + poder.controle_natureza) / 9
            return self.__tela_poder.mostra_mensagem(f"\033[1;33mA média de poder do detentor escolhido é: {media}\033[0m ")
        else:
            return self.__tela_poder.mostra_mensagem("\033[1;31mDETENTOR DO PODER INVÁLIDO. VERIFIQUE SE DIGITOU CORRETAMENTE \033[0m")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.inclui_poder,
            2: self.altera_poder,
            3: self.lista_poderes,
            4: self.exclui_poder,
            5: self.mostra_media_poder,
            0: self.retornar
        }
        continua = True
        while continua:
            lista_opcoes[self.__tela_poder.tela_opcoes()]()
