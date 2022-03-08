import PySimpleGUI as sg


class TelaDadosSistema():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Sistema de Gerenciamento de Super-Heróis')],
            [sg.Text('Atenção: antes de cadastrar uma missão, cadastre os integrantes dela (sencientes e clientes).')],
            [sg.Text('Escolha uma opção:')],
            [sg.Button('Missão'), sg.Button('Senciente (Super-Herói ou Vilão)'), sg.Button('Poder'),
             sg.Button('Cliente'), sg.Button('Finalizar Sistema')]
        ]

        self.__window = sg.Window('TelaInicial', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
