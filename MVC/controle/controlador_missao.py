#from
#from

class ControladorMissao():

    def __init__(self, controlador_sistema):
        self.__missoes = []
        self.__tarefas = []
        self.__tela_missao = TelaMissao()
        self.__controlador_sistema = controlador_sistema

    def incluir_missao(self, missao: Missao):
        missoes.append(missao)

    def alterar_missao(self):
        pass

    def gerar_resultado(self):
        pass

    def incluir_tarefa(self): # deixei o verbo no infinitivo
        pass

    def alterar_tarefa(self): # deixei o verbo no infinitivo
        pass

# Adições de métodos que estão na classe "Missao"

    def incluir_cliente(self, cliente: Cliente):
        pass

    def excluir_cliente(self, cliente: Cliente):
        pass

    def listar_tarefas(self):
        pass

    def incluir_super_heroi(self, super_heroi: SuperHeroi):
        pass

    def excluir_super_heroi(self, super_heroi: SuperHeroi):
        pass

    def listar_super_herois(self):
        pass

    def incluir_vilao(self, vilao: Vilao):
        pass

    def excluir_vilao(self, vilao: Vilao):
        pass

    def listar_viloes(self):
        pass

    def listar_detalhes(self):
        pass

