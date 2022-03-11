import PySimpleGUI as sg


class TelaDadosVilao():
    def __init__(self, controlador_senciente):
        self.__controlador_senciente = controlador_senciente
        self.__window = None
        self.init_components(dados_poder={"nome":"","fraqueza":"","local_moradia":"","periculosidade":""})

    def init_components(self, dados_poder):
        layout = [
            [sg.Text('Dados:')],
            [sg.Text('Nome:'), sg.InputText(dados_poder['nome'], key='nome')],
            [sg.Text('Fraqueza:'),sg.InputText(dados_poder['fraqueza'], key='fraqueza')],
            [sg.Text('Local de Moradia:'),sg.InputText(dados_poder['local_moradia'], key='local_moradia')],
            [sg.Text('Periculosidade:'),sg.InputText(dados_poder['periculosidade'], key='periculosidade')],
            [sg.Submit(button_text="Salvar"), sg.Cancel(button_text="Cancelar", )]
        ]
        self.__window = sg.Window('Dados dos Poderes').Layout(layout)

    def open(self, dados_vilao={"nome":"","fraqueza":"","local_moradia":"","periculosidade":""}):
        self.init_components(dados_vilao)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_opcoes(self):
        self.open()