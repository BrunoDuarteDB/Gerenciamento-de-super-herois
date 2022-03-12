import PySimpleGUI as sg


class TelaSencienteGUI():

    def __init__(self, controlador_senciente):
        self.__controlador_senciente = controlador_senciente
        self.__window = None
        self.init_components()

    def init_components(self, dict_super_herois=[], dict_viloes=[]):
        layout = [
            [sg.Text('Sencientes cadastrados:')],
            [sg.Text('Super-Heróis:')],
            [sg.Listbox(values=tuple(dict_super_herois), size=(30, 3), key='lb_itens')],
            [sg.Text('')],
            [sg.Text('Vilões:')],
            [sg.Listbox(values=tuple(dict_viloes), size=(30, 3), key='lb_itens')],
            [sg.Button('Incluir em Missão'), sg.Button('Novo Super-Herói'), sg.Button('Novo Vilão'),
             sg.Button('Alterar'), sg.Button('Excluir'),
             sg.Button('Retornar')]
        ]

        self.__window = sg.Window('TelaSenciente', default_element_size=(40, 1)).Layout(layout)

    def open(self, dicts):
        dict_super_herois = dicts[0]
        dict_viloes = dicts[1]
        button, values = self.__window.Read(dict_super_herois, dict_viloes)
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
