import PySimpleGUI as sg


class TelaDadosTarefa():
    def __init__(self, controlador_missao):
        self.__controlador_missao = controlador_missao
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Dados da Tarefa:')],
            [sg.Text("ID:"), sg.InputText(key='id')],
            [sg.Text("Descrição:"), sg.InputText(key='descricao')],
            [sg.Submit(button_text="Salvar"), sg.Submit(button_text="Salvar e incluir +1 tarefa")]
        ]
        self.__window = sg.Window('Dados da Tarefa').Layout(layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
