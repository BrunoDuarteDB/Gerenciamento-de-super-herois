
class TelaSenciente():
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print('---------- SENCIENTE ----------')
        print('Opções:')
        print('1 - Incluir Senciente')
        print('2 - Alterar Senciente')
        print('3 - Listar Sencientes')
        print('4 - Excluir Senciente')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def cadastrar_senciente(self):
        print('----- DADOS SENCIENTE -----')
        heroi_ou_vilao = int(input('Herói ou vilão? Digite 1 para Herói ou 2 para Vilão: '))
        nome = input('Nome: ')
        poder = None # COMO???
        fraqueza = input('Fraqueza: ')
        empresa = input('Empresa: ')
        local_moradia = ('Onde mora: ')

        return {"heroi_ou_vilao": heroi_ou_vilao, "nome": nome, "poder": poder, "fraqueza": fraqueza, "empresa": empresa, "local_moradia": local_moradia}

    def listar_sencientes(self):
        pass