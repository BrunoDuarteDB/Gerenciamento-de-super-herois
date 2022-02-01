from limite.tela_missao import TelaMissao
from entidade.missao import Missao

class ControladorMissao():

    def __init__(self, controlador_sistema):
        self.__missoes = []
        self.__tarefas = []
        self.__tela_missao = TelaMissao()
        self.__controlador_sistema = controlador_sistema

    def incluir_missao(self):
        dados_missao = self.__tela_missao.pega_dados_missao()
        missao = Missao(dados_missao['titulo'], dados_missao['data'], dados_missao['local'],
                        dados_missao['conflito'], dados_missao['clientes'], dados_missao['tarefas'],
                        dados_missao['super_herois'], dados_missao['vilao'])
        self.__missoes.append(missao)

    def alterar_missao(self):


    def gerar_resultado(self):
        pass

    def incluir_tarefa(self): # deixei o verbo no infinitivo
        pass

    def alterar_tarefa(self): # deixei o verbo no infinitivo
        pass

    def listar_tarefas(self):
        pass

    def listar_missao_fracasso(self):
        pass

    def listar_missao_sucesso(self):
        pass
