class DetentorAlteradoException(Exception):
    def __init__(self):
        super().__init__('Ops, o nome do detentor não pode ser alterado!')