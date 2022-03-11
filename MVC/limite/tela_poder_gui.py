import PySimpleGUI as sg

class TelaPoderGUI():

    def __init__(self, controlador_poder):
        self.__controlador_poder = controlador_poder
        self.__window = None
        self.init_components()

    def init_components(self, dados_poderes=[]):

        layout = [
            [sg.Text('Poderes:')],
            [sg.Spin(values=dados_poderes, size=(30, 3), key='lb_itens')],
            [sg.Submit(button_text='Incluir'), sg.Submit(button_text='Alterar'), sg.Submit(button_text='Excluir'),
             # sg.Submit(button_text='Retornar'),
             sg.Submit(button_text='Incluir em Senciente')]
        ]

        self.__window = sg.Window('TelaPoder', default_element_size=(40, 1)).Layout(layout)

    def open(self, dados_poderes=[]):
        self.init_components(dados_poderes)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)