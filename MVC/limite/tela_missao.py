

class TelaMissao():

    def __init__(self, controlador_missao):
        self.__controlador_missao = controlador_missao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print('----- MISSÃO -----')
        print('Opções:')
        print('1 - Incluir missão')
        print('2 - Alterar missão')
        print('3 - Excluir missão')
        print('4 - Listar missões bem sucedidas')
        print('5 - Listar missões fracassadas')
        print('0 - Retornar')

        while True:

            try:
                opcoes_validas = [0, 1, 2, 3, 4, 5]
                opcao = int(input("Escolha uma opção: "))
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Opção inválida!')



    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_missao(self):
        print('------ DADOS MISSÃO ------')
        titulo = input('Título: ')
        data = input('Data: ')
        local = input('Local: ')
        conflito = input('Conflito: ')

        return {'titulo': titulo, 'data': data, 'local': local, 'conflito': conflito}

    def pega_dados_tarefa(self):
        print('------ DADOS TAREFA ------')
        id_tarefa = input('Id da tarefa: ')
        descricao = input('Descrição da tarefa: ')

        return {'id_tarefa': id_tarefa, 'descricao': descricao}

    def selecionar_tarefa(self):
        id_tarefa = input('Id da tarefa que deseja selecionar: ')
        return id_tarefa

    def mostrar_missao(self, dados_missao):
        print("TÍTULO: ", dados_missao["titulo"])
        print("DATA: ", dados_missao["data"])
        print("LOCAL: ", dados_missao["local"])
        print("CONFLITO: ", dados_missao["conflito"])
        print("CLIENTES: ", dados_missao["clientes"])
        print("TAREFAS: ", dados_missao["tarefas"])
        print("SUPER HERÓIS: ", dados_missao["super_heroi"])
        print("VILÃO: ", dados_missao["vilao"])

    def mostrar_super_heroi(self, dados_super_heroi):
        print('NOME: ', dados_super_heroi['nome'])
        print('PODER: ', dados_super_heroi['poder'])
        print('FRAQUEZA: ', dados_super_heroi['fraqueza'])
        print('EMPRESA: ', dados_super_heroi['empresa'])
        print('LOCAL ONDE MORA: ', dados_super_heroi['local_moradia'])
        print('ALTEREGO: ', dados_super_heroi['alterego'])

    def mostrar_vilao(self, dados_vilao):
        print('NOME: ', dados_vilao['nome'])
        print('PODER: ', dados_vilao['poder'])
        print('FRAQUEZA: ', dados_vilao['fraqueza'])
        print('EMPRESA: ', dados_vilao['empresa'])
        print('LOCAL ONDE MORA: ', dados_vilao['local_moradia'])
        print('PERICULOSIDADE: ', dados_vilao['periculosidade'])

    def mostrar_tarefa(self, dados_tarefa):
        print('ID DA TAREFA: ', dados_tarefa['id_tarefa'])
        print('DESCRIÇÃO DA TAREFA: ', dados_tarefa['descricao'])

    def selecionar_missao(self):
        titulo = input("Título da missão que deseja selecionar: ")
        return titulo

    def mostrar_mensagem(self, msg):
        print(msg)
