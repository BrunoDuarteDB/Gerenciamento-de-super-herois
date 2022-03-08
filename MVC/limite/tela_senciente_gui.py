import PySimpleGUI as sg


class TelaDadosSenciente():

    def __init__(self, controlador_senciente):
        self.__controlador_senciente = controlador_senciente
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Sencientes cadastrados:')],
            [sg.Text('Super-Heróis:')],
            [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3), key='lb_itens')],
            [sg.Text('')],
            [sg.Text('Vilões:')],
            [sg.Listbox(values=('Listbox 4', 'Listbox 5', 'Listbox 6'), size=(30, 3), key='lb_itens')],
            [sg.Button('Incluir em Missão'), sg.Button('Novo Senciente'), sg.Button('Alterar'), sg.Button('Excluir'),
             sg.Button('Retornar')]
        ]

        self.__window = sg.Window('TelaSenciente', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)