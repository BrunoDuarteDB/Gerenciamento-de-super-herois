import PySimpleGUI as sg


class TelaClienteGUI():

    def __init__(self, controlador_cliente):
        self.__controlador_cliente = controlador_cliente
        self.__window = None
        self.init_components()

    def init_components(self, dados_clientes=[]):

        layout = [
            [sg.Text('Clientes:')],
            [sg.Listbox(values=dados_clientes, size=(30, 3), key='lb_itens')],
            [sg.Submit(button_text='Novo Cliente'), sg.Submit(button_text='Alterar'), sg.Submit(button_text='Excluir'),
             sg.Submit(button_text='Retornar'), sg.Submit(button_text='Incluir em Missão')]
        ]

        self.__window = sg.Window('TelaCliente', default_element_size=(40, 1)).Layout(layout)

    def open(self, dados_clientes=[]):
        self.init_components(dados_clientes)
        button, values = self.__window.Read()
        # self.close()
        print(button)
        return button

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)
