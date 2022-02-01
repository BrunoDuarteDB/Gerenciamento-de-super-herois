

class TelaMissao():
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

        opcao = int(input("Escolha uma opção: "))
        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_missao(self):
        print('------DADOS MISSÃO ------')
        titulo = input('Título: ')
        data = input('Data: ')
        local = input('Local: ')
        conflito = input('Conflito: ')
        clientes = None # COMO???
        tarefas = None # COMO???
        super_herois = None # COMO???
        vilao = None # COMO???

        return {'titulo': titulo, 'data': data, 'local': local, 'conflito': conflito, 'clientes': clientes,
                'tarefas': tarefas, 'super_herois': super_herois, 'vilao': vilao}