import PySimpleGUI as sg


class TelaDadosCliente():
    def __init__(self, controlador_cliente):
        self.__controlador_cliente = controlador_cliente
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Dados do Cliente:')],
            [sg.InputText('Nome/Título', key='nome'), sg.InputText('País de Origem', key='pais_origem')],
            [sg.InputText('Local de Sede', key='local_sede'), sg.InputText('Código', key='codigo')],
            [sg.Submit(button_text="Salvar")]
        ]
        self.__window = sg.Window('Dados do Cliente').Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_opcoes(self):
        self.open()