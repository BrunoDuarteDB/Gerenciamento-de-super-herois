from MVC.controle.controlador_senciente import ControladorSenciente

class TelaSenciente():

    def __init__(self, controlador_senciente):
        self.__controlador_senciente = controlador_senciente

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
    def pega_dados_senciente(self):
        print('----- DADOS SENCIENTE -----')
        heroi_ou_vilao = int(input('Herói ou vilão? Digite 1 para Herói ou 2 para Vilão: '))
        nome = input('Nome: ')
        poder = self.__inclui_poder_em_senciente()
        fraqueza = input('Fraqueza: ')
        empresa = input('Empresa: ')
        local_moradia = ('Onde mora: ')

        if heroi_ou_vilao == 1:
            alterego = input('Alterego: ')
            return {"nome": nome, "poder": poder, "fraqueza": fraqueza, "empresa": empresa,
                    "local_moradia": local_moradia, "alterego": alterego}

        elif heroi_ou_vilao == 2:
            periculosidade = input('Periculosidade: ')
            return {"nome": nome, "poder": poder, "fraqueza": fraqueza, "empresa": empresa,
                    "local_moradia": local_moradia, "periculosidade": periculosidade}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_senciente(self, dados_senciente):
        if isinstance(super_heroi, SuperHeroi):
            print('Nome do Super-Herói: ', dados_senciente['nome'])
            print('Fraqueza do Super-Herói: ', dados_senciente['fraqueza'])
            print('Empresa do Super-Herói: ', dados_senciente['empresa'])
            print('Local onde mora: ', dados_senciente['local_moradia'])
            print('Alterego do Super-Herói: ', dados_senciente['alterego'])
        elif isinstance(vilao, Vilao):
            print('Nome do Vilão: ', dados_senciente['nome'])
            print('Fraqueza do Vilão: ', dados_senciente['fraqueza'])
            print('Empresa do Vilão: ', dados_senciente['empresa'])
            print('Local onde mora: ', dados_senciente['local_moradia'])
            print('Periculosidade do Vilão: ', dados_senciente['periculosidade'])
        print('\n')

    def seleciona_senciente(self):
        nome = input('Nome do senciente (Super-Herói ou Vilão) que deseja selecionar: ')
        return nome

    def mostra_mensagem(self, mensagem):
        print(mensagem)