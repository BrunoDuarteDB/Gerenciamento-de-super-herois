class TelaSistema:

    def __init__(self, controlador_sistema):
        self.__controlador_senciente = controlador_sistema

    def tela_opcoes(self):
        print('\033[1;32m----- Sistema de Gerenciamento de Super-Heróis -----\033[0m')
        print('ATENÇÃO: antes de cadastrar uma missão, cadastre os integrantes dela (sencientes e clientes).')
        print('Opções:')
        print('\033[1;95m1 - Missão\033[0m')
        print('\033[1;96m2 - Senciente (Super-Herói ou Vilão)\033[0m')
        print('\033[1;94m3 - Poder\033[0m')
        print('\033[1;93m4 - Cliente\033[0m')
        print('0 - Finalizar sistema')

        while True:

            try:
                opcoes_validas = [0, 1, 2, 3, 4]
                opcao = int(input("Escolha uma opção: "))
                print()
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Opção inválida!')
                print()

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
