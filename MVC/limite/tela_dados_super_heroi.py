import PySimpleGUI as sg


class TelaDadosSuperHeroi():
    def __init__(self, controlador_senciente):
        self.__controlador_senciente = controlador_senciente
        self.__window = None
        self.init_components(
            dados_super_heroi={"nome": "", "fraqueza": "", "empresa": "", "local_moradia": "", "alterego": ""})

    def init_components(self, dados_super_heroi):
        layout = [
            [sg.Text('Dados:')],
            [sg.Text('Nome:', size=(13, 1)), sg.InputText(dados_super_heroi['nome'], key='nome')],
            [sg.Text('Fraqueza:', size=(13, 1)), sg.InputText(dados_super_heroi['fraqueza'], key='fraqueza')],
            [sg.Text('Empresa:', size=(13, 1)), sg.InputText(dados_super_heroi['empresa'], key='empresa')],
            [sg.Text('Local de Moradia:', size=(13, 1)), sg.InputText(dados_super_heroi['local_moradia'], key='local_moradia')],
            [sg.Text('Alter Ego:', size=(13, 1)), sg.InputText(dados_super_heroi['alterego'], key='alterego')],
            [sg.Submit(button_text="Salvar")]
        ]
        self.__window = sg.Window('Dados do Super-Herói').Layout(layout)

    def open(self, dados_super_heroi={"nome": "", "fraqueza": "", "empresa": "", "local_moradia": "", "alterego": ""}):
        self.init_components(dados_super_heroi)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
