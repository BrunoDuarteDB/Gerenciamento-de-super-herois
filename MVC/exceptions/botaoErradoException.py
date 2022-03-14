class BotaoErradoException(Exception):
    def __init__(self):
        super().__init__('Ops, você deve clicar em "Incluir em Missão" ou "Incluir mais Sencientes/Clientes"')
