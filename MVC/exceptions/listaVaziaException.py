class ListaVaziaException(Exception):
    def __init__(self):
        super().__init__("Ops, você esqueceu de selecionar algum senciente ou cliente!")