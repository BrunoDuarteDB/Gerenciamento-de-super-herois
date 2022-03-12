import PySimpleGUI as sg


class TelaDadosPoder():
    def __init__(self, controlador_poder):
        self.__controlador_poder = controlador_poder
        self.__window = None
        self.init_components(dados_poder={"detentor": "", "inteligencia": "", "velocidade": "", "artes_marciais": "",
                                          "forca": "", "fator_cura": "", "poder_magico": "", "expertise": "",
                                          "resistencia": "", "controle_natureza": ""})

    def init_components(self, dados_poder):
        layout = [
            [sg.Text('Poderes:')],
            [sg.Text('Detentor:'), sg.InputText(dados_poder['detentor'], key='detentor')],
            [sg.Text('Inteligência:'), sg.InputText(dados_poder['inteligencia'], key='inteligencia')],
            [sg.Text('Velocidade:'), sg.InputText(dados_poder['velocidade'], key='velocidade')],
            [sg.Text('Artes Marciais:'), sg.InputText(dados_poder['artes_marciais'], key='artes_marciais')],
            [sg.Text('Força:'), sg.InputText(dados_poder['forca'], key='forca')],
            [sg.Text('Fator Cura:'), sg.InputText(dados_poder['fator_cura'], key='fator_cura')],
            [sg.Text('Poder Mágico:'), sg.InputText(dados_poder['poder_magico'], key='poder_magico')],
            [sg.Text('Expertise:'), sg.InputText(dados_poder['expertise'], key='expertise')],
            [sg.Text('Resistência:'), sg.InputText(dados_poder['resistencia'], key='resistencia')],
            [sg.Text('Controle da Natureza:'), sg.InputText(dados_poder['controle_natureza'], key='controle_natureza')],
            [sg.Submit(button_text="Salvar"), sg.Cancel(button_text="Cancelar", )]
        ]
        self.__window = sg.Window('Dados dos Poderes').Layout(layout)

    def open(self, dados_poder):
        if isinstance(dados_poder, dict):
            self.init_components(dados_poder)
        elif isinstance(dados_poder, str):
            nome = dados_poder
            dados_poder = {'detentor': nome, "inteligencia": "", "velocidade": "", "artes_marciais": "",
                                          "forca": "", "fator_cura": "", "poder_magico": "", "expertise": "",
                                          "resistencia": "", "controle_natureza": ""}
            self.init_components(dados_poder)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_opcoes(self):
        self.open()
