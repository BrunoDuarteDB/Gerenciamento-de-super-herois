import PySimpleGUI as sg


class TelaMissaoGUI():

    def __init__(self, controlador_missao):
        self.__controlador_missao = controlador_missao
        self.__window = None
        self.init_components()

    def init_components(self, dict_missoes_sucesso=[], dict_missoes_fracasso=[]):
        layout = [
            [sg.Text('Missões Bem-sucedidas:')],
            [sg.Listbox(values=tuple(dict_missoes_sucesso), size=(30, 3), key='lb_itens')],
            [sg.Text('')],
            [sg.Text('Missões Fracassadas:')],
            [sg.Listbox(values=tuple(dict_missoes_fracasso), size=(30, 3), key='lb_itens')],
            [sg.Button('Incluir'), sg.Button('Alterar'), sg.Button('Excluir'), sg.Button('Retornar')]
        ]

        self.__window = sg.Window('TelaMissao', default_element_size=(40, 1)).Layout(layout)

    def open(self, dicts):
        if dicts[0] == None and dicts[1] == None:
            dict_missoes_sucesso = []
            dict_missoes_fracasso = []
        dict_missoes_sucesso = dicts[0]
        dict_missoes_fracasso = dicts[1]
        self.init_components(dict_missoes_sucesso, dict_missoes_fracasso)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, titulo: str, mensagem: str):
        sg.Popup(titulo, mensagem)