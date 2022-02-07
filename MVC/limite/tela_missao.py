

class TelaMissao():

    def __init__(self, controlador_missao):
        self.__controlador_missao = controlador_missao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print('\033[1;95m----- MISSÃO -----\033[0m')
        print('Opções:')
        print('1 - Incluir missão')
        print('2 - Alterar missão')
        print('3 - Excluir missão')
        print('4 - Listar missões bem sucedidas')
        print('5 - Listar missões fracassadas')
        print('6 - Listar todas as missões')
        print('0 - Retornar')

        while True:

            try:
                opcoes_validas = [0, 1, 2, 3, 4, 5, 6]
                opcao = int(input("Escolha uma opção: "))
                print()
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Opção inválida!')
                print()

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_missao(self):
        print('------ DADOS MISSÃO ------')
        while True:
            try:
                titulo = input("Título: ").strip()
                if titulo == "" or titulo.isdigit() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO. \033[0m")
        while True:
            try:
                data = input("Data: ").strip()
                if data == "":
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO. \033[0m")
        while True:
            try:
                local = input("Local: ").strip()
                if local == "" or local.isdigit() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO. \033[0m")
        while True:
            try:
                conflito = input('Conflito: ').strip()
                if conflito == "" or conflito.isdigit() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO. \033[0m")
        print()

        return {'titulo': titulo, 'data': data, 'local': local, 'conflito': conflito}

    def pega_dados_tarefa(self):
        print('------ DADOS TAREFA ------')
        while True:
            try:
                id_tarefa = input('ID da tarefa: ').strip()
                if id_tarefa == "" or id_tarefa.isalpha() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO. \033[0m")
        while True:
            try:
                descricao = input('Descrição da tarefa: ').strip()
                if descricao == "" or descricao.isalpha() is False:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO. \033[0m")
        print()

        return {'id_tarefa': id_tarefa, 'descricao': descricao}

    def selecionar_tarefa(self):
        id_tarefas = []
        for tarefa in self.__controlador_missao.tarefas:
            id_tarefas.append(tarefa.id_tarefa)
        while True:
            try:
                id_tarefa = input('ID da tarefa que deseja selecionar: ').strip()
                if id_tarefa not in id_tarefas:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! ESSA TAREFA NÃO EXISTE. \033[0m")
        print()
        return id_tarefa

    def mostrar_missao(self, dados_missao):
        print("Título: ", dados_missao["titulo"])
        print("Data: ", dados_missao["data"])
        print("Local: ", dados_missao["local"])
        print("Conflito: ", dados_missao["conflito"])
        print("Clientes: ", dados_missao["clientes"])
        print("Tarefas: ", dados_missao["tarefas"])
        print("Super-Heróis: ", dados_missao["super_herois"])
        print("Vilões: ", dados_missao["viloes"])
        print("Resultado: ", dados_missao["resultado"])
        print()

    def mostrar_super_heroi(self, dados_super_heroi):
        print('NOME: ', dados_super_heroi['nome'])
        print('PODER: ', dados_super_heroi['poder'])
        print('FRAQUEZA: ', dados_super_heroi['fraqueza'])
        print('EMPRESA: ', dados_super_heroi['empresa'])
        print('LOCAL ONDE MORA: ', dados_super_heroi['local_moradia'])
        print('ALTEREGO: ', dados_super_heroi['alterego'])
        print()

    def mostrar_vilao(self, dados_vilao):
        print('NOME: ', dados_vilao['nome'])
        print('PODER: ', dados_vilao['poder'])
        print('FRAQUEZA: ', dados_vilao['fraqueza'])
        print('EMPRESA: ', dados_vilao['empresa'])
        print('LOCAL ONDE MORA: ', dados_vilao['local_moradia'])
        print('PERICULOSIDADE: ', dados_vilao['periculosidade'])
        print()

    def mostrar_tarefa(self, dados_tarefa):
        print('ID DA TAREFA: ', dados_tarefa['id_tarefa'])
        print('DESCRIÇÃO DA TAREFA: ', dados_tarefa['descricao'])
        print()

    def selecionar_missao(self):
        titulos = []
        for missao in self.__controlador_missao.missoes:
            titulos.append(missao.titulo)
        while True:
            try:
                titulo = input('Título da missão que deseja selecionar: ').strip()
                if titulo not in titulos:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! ESSA MISSÃO NÃO EXISTE. \033[0m")
        print()
        return titulo

    def deseja_mais_tarefa(self):
        while True:
            try:
                pergunta = input('Deseja adicionar mais uma tarefa? (S/N): ')
                if pergunta not in {"S", "s", "N", "n"}:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mRESPOSTA INVÁLIDA. DIGITE S OU N \033[0m")
        print()
        return pergunta

    def deseja_mais_super_heroi(self):
        while True:
            try:
                pergunta = input('Deseja adicionar mais um super-herói? (S/N): ')
                if pergunta not in {"S", "s", "N", "n"}:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mRESPOSTA INVÁLIDA. DIGITE S OU N \033[0m")
        print()
        return pergunta

    def deseja_mais_vilao(self):
        while True:
            try:
                pergunta = input('Deseja adicionar mais um vilão? (S/N): ')
                if pergunta not in {"S", "s", "N", "n"}:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mRESPOSTA INVÁLIDA. DIGITE S OU N \033[0m")
        print()
        return pergunta

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
