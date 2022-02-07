from MVC.limite.tela_missao import TelaMissao
from MVC.entidade.missao import Missao
from MVC.entidade.tarefa import Tarefa
from random import randint


class ControladorMissao:

    def __init__(self, controlador_sistema):
        self.__missoes = []
        self.__tarefas = []
        self.__tela_missao = TelaMissao(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def tarefas(self):
        return self.__tarefas

    @property
    def missoes(self):
        return self.__missoes

    def pegar_missao_por_titulo(self, titulo: str):
        for missao in self.__missoes:
            if (missao.titulo== titulo):
                return missao
        return None

    def incluir_missao(self):
        dados_missao = self.__tela_missao.pega_dados_missao()
        clientes = self.pede_seleciona_cliente()
        tarefas = self.pede_seleciona_tarefa()
        super_herois = self.pede_seleciona_super_heroi()
        viloes = self.pede_seleciona_vilao()
        missao = Missao(dados_missao['titulo'], dados_missao['data'], dados_missao['local'],
                        dados_missao['conflito'], clientes, tarefas, super_herois, viloes)
        resultado = self.gerar_resultado(super_herois, viloes)
        missao.resultado = resultado
        self.__missoes.append(missao)
        self.listar_missao(missao)

        # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def listar_missao(self, missao):
        clientes = []
        tarefas = []
        super_herois = []
        viloes = []

        for b in missao.clientes:
            clientes.append(b.nome)
        for c in missao.tarefas:
            tarefas.append(c.descricao)
        for d in missao.super_herois:
            super_herois.append(d.nome)
        for e in missao.viloes:
            viloes.append(e.nome)

        self.__tela_missao.mostrar_missao({
            "titulo": missao.titulo,
            "data": missao.data,
            "local": missao.local,
            "conflito": missao.conflito,
            "clientes": clientes,
            "tarefas": tarefas,
            "super_herois": super_herois,
            "viloes": viloes,
            "resultado": missao.resultado
            })

    def excluir_missao(self):
        self.listar_missoes()
        titulo_missao = self.__tela_missao.selecionar_missao()
        missao = self.pegar_missao_por_titulo(titulo_missao)

        if missao is not None:
            self.__missoes.remove(missao)
            self.listar_missoes()
        else:
            self.__tela_missao.mostrar_mensagem("ATENÇÃO: Missão não existe, verifique se digitou corretamente.")

    def listar_missoes(self):
        for m in self.__missoes:
            clientes = []
            tarefas = []
            super_herois = []
            viloes = []
            for b in m.clientes:
                clientes.append(b.nome)
            for c in m.tarefas:
                tarefas.append(c.descricao)
            for d in m.super_herois:
                super_herois.append(d.nome)
            for e in m.viloes:
                viloes.append(e.nome)

            self.__tela_missao.mostrar_missao({
                "titulo": m.titulo,
                "data": m.data,
                "local": m.local,
                "conflito": m.conflito,
                "clientes": clientes,
                "tarefas": tarefas,
                "super_herois": super_herois,
                "viloes": viloes,
                "resultado": m.resultado
            })

    def alterar_missao(self):
        self.listar_missoes()
        titulo = self.__tela_missao.selecionar_missao()
        missao = self.pegar_missao_por_titulo(titulo)


        if missao is not None:
            novos_dados_missao= self.__tela_missao.pega_dados_missao()
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
            self.__tela_missao.mostrar_mensagem("ATENÇÃO: Missão não existente. Verifique se digitou corretamente.")

    def gerar_resultado(self, super_herois, viloes):
        media_super_herois = 0
        media_viloes = 0
        for super_heroi in super_herois:
            media_super_herois += super_heroi.poder.media_poder
        for vilao in viloes:
            media_viloes += vilao.poder.media_poder

        aleatorio_super_heroi = randint(1, 10)
        aleatorio_vilao = randint(1, 10)

        total_super_herois = media_super_herois * aleatorio_super_heroi
        total_viloes = media_viloes * aleatorio_vilao

        if total_super_herois > total_viloes:
            return 'sucesso'
        elif total_viloes > total_super_herois:
            return 'fracasso'

    def incluir_tarefa(self): # deixei o verbo no infinitivo
        dados_tarefa = self.__tela_missao.pega_dados_tarefa()
        tarefa = Tarefa(dados_tarefa['id_tarefa'], dados_tarefa['descricao'])
        self.__tarefas.append(tarefa)
        return tarefa

    def alterar_tarefa(self): # deixei o verbo no infinitivo
        self.listar_tarefas()
        id_tarefa = self.__tela_missao.selecionar_tarefa()
        tarefa = self.pega_tarefa_por_id(id_tarefa)

        if tarefa is not None:
            novos_dados_tarefa = self.__tela_missao.pega_dados_tarefa()
            tarefa.id_tarefa = novos_dados_tarefa['id_tarefa']
            tarefa.descricao = novos_dados_tarefa['descricao']
            self.listar_tarefas()
        else:
            self.__tela_missao.mostrar_mensagem("Atenção: tarefa não existente!")

    def listar_tarefas(self):
        for tarefa in self.__tarefas:
            self.__tela_missao.mostrar_tarefa({'id_tarefa': tarefa.id_tarefa, 'descricao': tarefa.descricao})

    def checar_lista_tarefas(self):
        if len(self.__tarefas) == 0:
            return 0

    def pega_tarefa_por_id(self, id_tarefa: str):
        for tarefa in self.__tarefas:
            if tarefa.id_tarefa == id_tarefa:
                return tarefa
        return None

    def listar_missao_fracasso(self):
        fracassadas = []
        for m in self.__missoes:
            if m.resultado == 'fracasso':
                fracassadas.append(m)

        for m in fracassadas:
            clientes = []
            tarefas = []
            super_herois = []
            viloes = []

            for b in m.clientes:
                clientes.append(b.nome)
            for c in m.tarefas:
                tarefas.append(c.descricao)
            for d in m.super_herois:
                super_herois.append(d.nome)
            for e in m.viloes:
                viloes.append(e.nome)

            self.__tela_missao.mostrar_missao({
                "titulo": m.titulo,
                "data": m.data,
                "local": m.local,
                "conflito": m.conflito,
                "clientes": clientes,
                "tarefas": tarefas,
                "super_herois": super_herois,
                "viloes": viloes,
                "resultado": m.resultado
            })

    def listar_missao_sucesso(self):
        bem_sucedidas = []
        for m in self.__missoes:
            if m.resultado == 'sucesso':
                bem_sucedidas.append(m)

        for m in bem_sucedidas:
            clientes = []
            tarefas = []
            super_herois = []
            viloes = []

            for b in m.clientes:
                clientes.append(b.nome)
            for c in m.tarefas:
                tarefas.append(c.descricao)
            for d in m.super_herois:
                super_herois.append(d.nome)
            for e in m.viloes:
                viloes.append(e.nome)

            self.__tela_missao.mostrar_missao({
                "titulo": m.titulo,
                "data": m.data,
                "local": m.local,
                "conflito": m.conflito,
                "clientes": clientes,
                "tarefas": tarefas,
                "super_herois": super_herois,
                "viloes": viloes,
                "resultado": m.resultado
            })

    def pede_seleciona_cliente(self):
        tamanho = len(self.__controlador_sistema.controlador_cliente.clientes)
        clientes = []
        cliente = self.__controlador_sistema.controlador_cliente.seleciona_cliente()
        clientes.append(cliente)
        if tamanho > 1:
            resposta = self.__controlador_sistema.controlador_cliente.deseja_mais()
            while resposta == "S":
                cliente = self.__controlador_sistema.controlador_cliente.seleciona_cliente()
                clientes.append(cliente)
                resposta = self.__controlador_sistema.controlador_cliente.deseja_mais()
        return clientes

    def pede_seleciona_tarefa(self):
        tarefas = []
        tarefa = self.incluir_tarefa()
        tarefas.append(tarefa)
        resposta = self.__tela_missao.deseja_mais_tarefa()
        while resposta == 'S':
            tarefa = self.incluir_tarefa()
            tarefas.append(tarefa)
            resposta = self.__tela_missao.deseja_mais_tarefa()
        return tarefas

    def pede_seleciona_super_heroi(self):
        tamanho = len(self.__controlador_sistema.controlador_senciente.super_herois)
        super_herois = []
        super_heroi = self.__controlador_sistema.controlador_senciente.seleciona_super_heroi()
        super_herois.append(super_heroi)
        if tamanho > 1:
            resposta = self.__tela_missao.deseja_mais_super_heroi()
            while resposta == 'S':
                super_heroi = self.__controlador_sistema.controlador_senciente.seleciona_super_heroi()
                super_herois.append(super_heroi)
                resposta = self.__tela_missao.deseja_mais_super_heroi()
        return super_herois

    def pede_seleciona_vilao(self):
        tamanho = len(self.__controlador_sistema.controlador_senciente.viloes)
        viloes = []
        vilao = self.__controlador_sistema.controlador_senciente.seleciona_vilao()
        viloes.append(vilao)
        if tamanho > 1:
            resposta = self.__tela_missao.deseja_mais_vilao()
            while resposta == 'S':
                vilao = self.__controlador_sistema.controlador_senciente.seleciona_vilao()
                viloes.append(vilao)
                resposta = self.__tela_missao.deseja_mais_vilao()
        return viloes

    '''def incluir_cliente(self, cliente: Cliente):
        pass

    def excluir_cliente(self, cliente: Cliente):
        pass

    def incluir_super_heroi(self, super_heroi: SuperHeroi):
        pass

    def excluir_super_heroi(self, super_heroi: SuperHeroi):
        pass

    def incluir_vilao(self, vilao: Vilao):
        pass

    def excluir_vilao(self, vilao: Vilao):
        pass'''

    def listar_viloes(self):
        for vilao in missao.viloes:
            self.__tela_missao.mostrar_vilao({'nome': vilao.nome,
                                              'poder': vilao.poder,
                                              'fraqueza': vilao.fraqueza,
                                              'empresa': vilao.empresa,
                                              'local_moradia': vilao.local_moradia,
                                              'periculosidade': vilao.periculosidade})

    def listar_super_herois(self):
        for super_heroi in missao.super_herois:
            self.__tela_missao.mostrar_super_heroi({'nome': super_heroi.nome,
                                                    'poder': super_heroi.poder,
                                                    'fraqueza': super_heroi.fraqueza,
                                                    'empresa': super_heroi.empresa,
                                                    'local_moradia': super_heroi.local_moradia,
                                                    'alterego': super_heroi.alterego})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes= {
            1: self.incluir_missao,
            2: self.alterar_missao,
            3: self.excluir_missao,
            4: self.listar_missao_sucesso,
            5: self.listar_missao_fracasso,
            0: self.retornar
        }
        continua=True
        while continua:
            lista_opcoes[self.__tela_missao.tela_opcoes()]()

