import PySimpleGUI as sg


class TelaDadosCliente():
    def __init__(self, controlador_cliente):
        self.__controlador_cliente = controlador_cliente
        self.__window = None
        self.init_components(dados_cliente={"codigo": "", "nome": "", "pais_origem": "", "local_sede": ""})

    def init_components(self, dados_cliente):
        layout = [
            [sg.Text('Dados do Cliente:')],
            [sg.Text("Nome:"), sg.InputText(dados_cliente["nome"], key='nome')],
            [sg.Text("País de Origem:"), sg.InputText(dados_cliente["pais_origem"], key='pais_origem')],
            [sg.Text("Local de Sede:"), sg.InputText(dados_cliente["local_sede"], key='local_sede')],
            [sg.Text("Código:"), sg.InputText(dados_cliente["codigo"], key='codigo')],
            [sg.Submit(button_text="Salvar")]
        ]
        self.__window = sg.Window('Dados do Cliente').Layout(layout)

    def open(self, dados_cliente):
        self.init_components(dados_cliente)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()
