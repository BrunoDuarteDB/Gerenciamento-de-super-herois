import PySimpleGUI as sg


class TelaDadosVilao():
    def __init__(self, controlador_senciente):
        self.__controlador_senciente = controlador_senciente
        self.__window = None
        self.init_components(
            dados_vilao={"nome": "", "fraqueza": "", "empresa": "", "local_moradia": "", "periculosidade": ""})

    def init_components(self, dados_vilao):
        layout = [
            [sg.Text('Dados:')],
            [sg.Text('Nome:', size=(13, 1)), sg.InputText(dados_vilao['nome'], key='nome')],
            [sg.Text('Fraqueza:', size=(13, 1)), sg.InputText(dados_vilao['fraqueza'], key='fraqueza')],
            [sg.Text('Empresa:', size=(13, 1)), sg.InputText(dados_vilao['empresa'], key='empresa')],
            [sg.Text('Local de Moradia:', size=(13, 1)), sg.InputText(dados_vilao['local_moradia'], key='local_moradia')],
            [sg.Text('Periculosidade:', size=(13, 1)), sg.InputText(dados_vilao['periculosidade'], key='periculosidade')],
            [sg.Submit(button_text="Salvar")]
        ]
        self.__window = sg.Window('Dados dos Poderes').Layout(layout)

    def open(self, dados_vilao={"nome": "", "fraqueza": "", "empresa": "", "local_moradia": "", "periculosidade": ""}):
        self.init_components(dados_vilao)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
