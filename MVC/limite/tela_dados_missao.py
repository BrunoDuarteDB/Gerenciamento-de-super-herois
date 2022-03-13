import PySimpleGUI as sg


class TelaDadosMissao():
    def __init__(self, controlador_missao):
        self.__controlador_cliente = controlador_missao
        self.__window = None
        self.init_components(dados_missao={"titulo":"","data":"","local":"","conflito":""})

    def init_components(self, dados_missao):
        layout = [
            [sg.Text('Dados da Missão:')],
            [sg.Text("Título:"), sg.InputText(dados_missao["titulo"], key='titulo')],
            [sg.Text("Data:"), sg.InputText(dados_missao["data"], key='data')],
            [sg.Text("Local:"), sg.InputText(dados_missao["local"], key='local')],
            [sg.Text("Conflito:"), sg.InputText(dados_missao["conflito"], key='conflito')],
            [sg.Submit(button_text="Salvar")]
        ]
        self.__window = sg.Window('Dados da Missão').Layout(layout)

    def open(self, dados_missao):
        self.init_components(dados_missao)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_opcoes(self):
        self.open()