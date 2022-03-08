import PySimpleGUI as sg


class TelaClienteGUI():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Clientes:')],
            [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3), key='lb_itens')],
            [sg.Button('Novo Cliente'), sg.Button('Alterar'), sg.Button('Excluir'), sg.Button('Retornar'),
             sg.Button('Incluir em Missão')]
        ]

        self.__window = sg.Window('TelaCliente', default_element_size=(40, 1)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
