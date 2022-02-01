class TelaSistema:
    # fazer aqui tratamento dos dados se a entrada de dados for diferente do esperado
    def tela_opcoes(self):
        print('----- Sistema de Gerenciamento de Super-Heróis -----')
        print('Opções:')
        print('1 - Super-Herói')
        print('2 - Vilão')
        print('3 - Poder')
        print('4 - Cliente')
        print('5 - Missão')
        print('0 - Finalizar sistema')
        opcao = int(input('Escolha uma opção: '))
        return opcao