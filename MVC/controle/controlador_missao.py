from MVC.limite.tela_missao_gui import TelaMissaoGUI
from MVC.limite.tela_dados_missao import TelaDadosMissao
from MVC.limite.tela_dados_tarefa import TelaDadosTarefa
from MVC.entidade.missao import Missao
from MVC.entidade.tarefa import Tarefa
from MVC.exceptions.listaVaziaException import ListaVaziaException
from MVC.persistencia.missao_dao import MissaoDAO
from MVC.persistencia.tarefa_dao import TarefaDAO
from random import randint


class ControladorMissao:

    def __init__(self, controlador_sistema):
        self.__tela_missao_gui = TelaMissaoGUI(self)
        self.__tela_dados_tarefa = TelaDadosTarefa(self)
        self.__tela_dados_missao = TelaDadosMissao(self)
        self.__controlador_sistema = controlador_sistema
        self.__missao_dao = MissaoDAO()
        self.__tarefa_dao = TarefaDAO()

    @property
    def tarefas(self):
        return self.__tarefa_dao.get_all()

    @property
    def missoes(self):
        return self.__missao_dao.get_all()

    def incluir_missao(self, values):
        while True:
            button, values = self.__tela_dados_missao.open(dados_missao={"titulo":"","data":"","local":"","conflito":""})
            self.__tela_dados_missao.close()

            try:
                if values == {"titulo":"","data":"","local":"","conflito":""} or (values["titulo"]).isdigit() == True \
                        or (values["local"]).isdigit() == True or (values["conflito"]).isdigit() == True:
                    raise ValueError
                break
            except ValueError:
                self.__tela_missao_gui.show_message('Atenção', 'Valor(es) inválido(s), tente novamente!')
                continue

        tarefas = self.incluir_tarefa()

        while True:
            sencientes = self.pede_seleciona_senciente() # BOTAOERRADOEXCEPTION AQUI TAMBÉM AAAAAAAAAAAAAAAAAAA
            try:
                if sencientes == []:
                    raise ListaVaziaException
                break
            except ListaVaziaException:
                self.__tela_missao_gui.show_message('Ops',"Você esqueceu de selecionar algum senciente!")
                continue

        lista_super_herois = []
        lista_viloes = []
        for i in range(len(sencientes)):
            for super_heroi in self.__controlador_sistema.controlador_senciente.super_herois:
                if super_heroi.nome == sencientes[i][0]:
                    lista_super_herois.append(super_heroi)
            for vilao in self.__controlador_sistema.controlador_senciente.viloes:
                if vilao.nome == sencientes[i][0]:
                    lista_viloes.append(vilao)

        while True:
            clientes = self.pede_seleciona_cliente()
            try:
                if clientes == []:
                    raise ListaVaziaException
                break
            except ListaVaziaException:
                self.__tela_missao_gui.show_message('Ops',"Você esqueceu de selecionar algum cliente!")
                continue

        lista_clientes = []
        for i in range(len(clientes)):
            for cliente in self.__controlador_sistema.controlador_cliente.clientes:
                if cliente.nome == clientes[i][0]:
                    lista_clientes.append(cliente)

        missao = Missao(values['titulo'], values['data'], values['local'],
                        values['conflito'], lista_clientes, tarefas, lista_super_herois, lista_viloes)
        resultado = self.gerar_resultado(lista_super_herois, lista_viloes)
        missao.resultado = resultado
        self.__missao_dao.persist(missao)
        self.__tela_dados_missao.close()
        self.__tela_missao_gui.close()

    def monta_dict_missoes_sucesso(self):
        sucesso = []
        for missao in self.__missao_dao.get_all():
            if missao.resultado == 'sucesso':
                sucesso.append(missao.titulo)
        return sucesso

    def monta_dict_missoes_fracasso(self):
        fracasso = []
        for missao in self.__missao_dao.get_all():
            if missao.resultado == 'fracasso':
                fracasso.append(missao.titulo)
        return fracasso

    def excluir_missao(self, dados_missao):
        if self.__missao_dao.get_all() == []:
            self.__tela_missao_gui.show_message("Atenção!", "Ainda não há missão cadastradas.")

        titulo_missao_excluida = dados_missao['lb_itens'][0]

        for missao in self.__missao_dao.get_all():
            if missao.titulo == titulo_missao_excluida:
                self.__missao_dao.remove(missao)
                del missao

        self.__tela_missao_gui.close()

    '''def alterar_missao(self):
        if self.__missoes == []:
            self.__tela_missao.mostrar_mensagem("\033[1;31mATENÇÃO: Ainda não há missões cadastradas.\033[0m")
            print()
            self.abre_tela()

        self.listar_missoes()
        titulo = self.__tela_missao.selecionar_missao()
        missao = self.pegar_missao_por_titulo(titulo)

        if missao is not None:
            novos_dados_missao = self.__tela_missao.pega_dados_missao()
            missao.titulo = novos_dados_missao["titulo"]
            missao.data = novos_dados_missao["data"]
            missao.local = novos_dados_missao["local"]
            missao.conflito = novos_dados_missao["conflito"]
            missao.clientes = novos_dados_missao["clientes"]
            missao.tarefas = novos_dados_missao["tarefas"]
            missao.super_herois = novos_dados_missao["super_herois"]
            missao.viloes = novos_dados_missao["viloes"]
            self.listar_missao()
        else:
            self.__tela_missao.mostrar_mensagem("ATENÇÃO: Missão não existente. Verifique se digitou corretamente.")'''

    def gerar_resultado(self, super_herois, viloes):
        media_super_herois = 0
        media_viloes = 0
        periculosidades = 0
        for super_heroi in super_herois:
            media_super_herois += super_heroi.poder.media_poder
        for vilao in viloes:
            media_viloes += vilao.poder.media_poder
        for vilao in viloes:
            periculosidades += vilao.periculosidade

        aleatorio_super_heroi = randint(1, 10)
        aleatorio_vilao = randint(1, 10)

        total_super_herois = media_super_herois * aleatorio_super_heroi
        total_viloes = media_viloes * aleatorio_vilao
        total_viloes += periculosidades

        if total_super_herois > total_viloes:
            return 'sucesso'
        elif total_viloes > total_super_herois:
            return 'fracasso'
        elif total_viloes == total_super_herois:
            return 'empate'

    def incluir_tarefa(self):
        tarefas = []
        button = 'Salvar e incluir +1 tarefa'
        while button == 'Salvar e incluir +1 tarefa':
            while True:
                button, values = self.__tela_dados_tarefa.open()
                self.__tela_dados_tarefa.close()

                try:
                    if (values['id']).isalpha() == True or (values['descricao']).isdigit() == True:
                        raise ValueError
                    values['id'] = int(values['id'])
                    tarefa = Tarefa(values['id'], values['descricao'])
                    tarefas.append(tarefa)
                    self.__tarefa_dao.persist(tarefa)
                    break
                except ValueError:
                    self.__tela_missao_gui.show_message('Atenção', 'Valor(es) inválido(s), tente novamente!')
                    continue
        return tarefas

    '''def alterar_tarefa(self):
        self.listar_tarefas()
        id_tarefa = self.__tela_missao.selecionar_tarefa()
        tarefa = self.pega_tarefa_por_id(id_tarefa)

        if tarefa is not None:
            novos_dados_tarefa = self.__tela_missao.pega_dados_tarefa()
            tarefa.id_tarefa = novos_dados_tarefa['id_tarefa']
            tarefa.descricao = novos_dados_tarefa['descricao']
            self.listar_tarefas()
        else:
            self.__tela_missao.mostrar_mensagem("Atenção: tarefa não existente!")'''

    def pede_seleciona_cliente(self):
        self.__tela_missao_gui.show_message('Atenção!', 'Selecione um cliente que você queira que '
                                                        'esteja na missão e, depois, clique em "Incluir em Missão"! Se'
                                                        'desejar incluir mais vezes, clique em "Incluir mais '
                                                        'Clientes"!')
        clientes = self.__controlador_sistema.controlador_cliente.seleciona_cliente()
        return clientes

    def pede_seleciona_senciente(self):
        self.__tela_missao_gui.show_message('Atenção!', 'Selecione um super-herói e um vilão que você queira que '
                                                        'esteja na missão e, depois, clique em "Incluir sencientes"! Se'
                                                        ' desejar incluir mais vezes, clique em "Incluir mais '
                                                        'Sencientes"!')
        sencientes = self.__controlador_sistema.controlador_senciente.seleciona_senciente()
        return sencientes

    def mostrar_detalhes(self, values):
        clientes = []
        tarefas = []
        super_herois = []
        viloes = []
        titulo_desejado = values['lb_itens'][0]
        for missao in self.__missao_dao.get_all():
            if missao.titulo == titulo_desejado:
                data = missao.data
                local = missao.local
                conflito = missao.conflito

                for cliente in missao.clientes:
                    clientes.append(cliente.nome)

                for tarefa in missao.tarefas:
                    tarefas.append(tarefa.descricao)

                for super_heroi in missao.super_herois:
                    super_herois.append(super_heroi.nome)

                for vilao in missao.viloes:
                    viloes.append(vilao.nome)

                resultado = missao.resultado

        self.__tela_missao_gui.close()
        self.__tela_missao_gui.show_message("Detalhes da Missão:", f'Título: {titulo_desejado}, Data: {data}  Local: {local}, Conflito: {conflito}, Clientes: {clientes}, Tarefas: {tarefas}, Super-Herói(s): {super_herois}, Vilão(ões): {viloes}, Resultado: {resultado}')

    def retornar(self, values):
        self.__tela_missao_gui.close()
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            "Incluir": self.incluir_missao,
            # "Alterar": self.alterar_missao,
            "Excluir": self.excluir_missao,
            "Mostrar Detalhes": self.mostrar_detalhes,
            "Retornar": self.retornar
        }

        continua = True
        while continua:
            dict_sucesso = self.monta_dict_missoes_sucesso()
            dict_fracasso = self.monta_dict_missoes_fracasso()
            button, values = self.__tela_missao_gui.open([dict_sucesso, dict_fracasso])
            lista_opcoes[button](values)

            # lista_opcoes[self.__tela_missao.tela_opcoes()]()
