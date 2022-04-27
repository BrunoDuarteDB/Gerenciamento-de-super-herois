class NadaSelecionadoException(Exception):
    def __init__(self):
        super().__init__("Ops, você não selecionou entidade alguma!")