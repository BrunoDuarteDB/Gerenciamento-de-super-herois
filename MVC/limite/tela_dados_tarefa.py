import PySimpleGUI as sg

class TelaDadosTarefa():
    def __init__(self, controlador_missao):
        self.__controlador_missao = controlador_missao
        self.__window = None
        self.init_components(dados_tarefa={"id":"","descricao":""})

    def init_components(self, dados_tarefa):
        layout = [
            [sg.Text('Dados da Tarefa:')],
            [sg.Text("ID:"), sg.InputText(dados_tarefa["id"], key='id')],
            [sg.Text("Descrição:"), sg.InputText(dados_tarefa["descricao"], key='descricao')],
            [sg.Submit(button_text="Salvar")]
        ]
        self.__window = sg.Window('Dados da Tarefa').Layout(layout)

    def open(self, dados_tarefa):
        self.init_components(dados_tarefa)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_opcoes(self):
        self.open()