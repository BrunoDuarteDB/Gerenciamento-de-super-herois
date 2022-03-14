class MissaoSemIntegrantesException(Exception):
    def __init__(self):
        super().__init__("Ops, você primeiro deve cadastrar pelo menos um Super-Herói e um cliente!")
