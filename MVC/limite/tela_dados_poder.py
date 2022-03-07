import PySimpleGUI as sg


class TelaDadosPoder():
    def __init__(self, controlador_poder):
        self.__controlador_poder = controlador_poder
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Poderes:')],
            [sg.InputText('Detentor', key='detentor'), sg.InputText('Inteligência', key='inteligencia')],
            [sg.InputText('Velocidade', key='velocidade'), sg.InputText('Artes Marciais', key='artes_marciais')],
            [sg.InputText('Força', key='forca'), sg.InputText('Fator Cura', key='fator cura')],
            [sg.InputText('Poder Mágico', key='poder_magico'), sg.InputText('Expertise', key='expertise')],
            [sg.InputText('Resistência', key='resistencia'),
             sg.InputText('Controle da Natureza', key='controle_natureza')],
            [sg.Submit(button_text="Salvar"), sg.Cancel(button_text="Cancelar", )]
        ]  # deixar ou tirar o cancel?
        self.__window = sg.Window('Dados dos Poderes').Layout(layout)

    def open(self):
        botao, valores = self.__window.Read()
        if botao == None:
            botao = 0
        return botao

    def close(self):
        self.__window.Close()

    def mostra_opcoes(self):
        self.open()




