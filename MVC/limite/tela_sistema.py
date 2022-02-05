class TelaSistema:
    # fazer aqui tratamento dos dados se a entrada de dados for diferente do esperado
    def tela_opcoes(self):
        print('\033[1;32m ----- Sistema de Gerenciamento de Super-Heróis -----\033[0m')
        print('ATENÇÃO: antes de cadastrar uma missão, cadastre os integrantes dela (sencientes e clientes).')
        print('Opções:')
        print('1 - Missão')
        print('2 - Senciente (Super-Herói ou Vilão)')
        print('3 - Poder')
        print('4 - Cliente')
        print('0 - Finalizar sistema')
        opcao = int(input('Escolha uma opção: '))
        return opcao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)