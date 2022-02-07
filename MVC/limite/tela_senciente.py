from MVC.entidade.super_heroi import SuperHeroi
from MVC.entidade.vilao import Vilao


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

        while True:

            try:
                opcoes_validas = [0, 1, 2, 3, 4]
                opcao = int(input("Escolha uma opção: "))
                print('\n')
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Opção inválida!')
                print('\n')

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_senciente(self):
        print('----- DADOS SENCIENTE -----')
        while True:
            try:
                heroi_ou_vilao = int(input('Herói ou vilão? Digite 1 para Herói ou 2 para Vilão: ').strip())
                numeros_possiveis = [1, 2]
                if heroi_ou_vilao not in numeros_possiveis:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mOPÇÃO INVÁLIDA! DIGITE 1 OU 2 \033[0m")
        while True:
            try:
                nome = input('Nome: ')
                if nome == "":
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! NÃO DEIXE O CAMPO VAZIO \033[0m")
        poder = self.__controlador_senciente.pede_cadastro_poder()
        while True:
            try:
                fraqueza = input('Fraqueza ("kryptonita, por exemplo"): ')
                if fraqueza == "":
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! NÃO DEIXE O CAMPO VAZIO \033[0m")
        while True:
            try:
                empresa = input('Empresa: ')
                if empresa == "":
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! NÃO DEIXE O CAMPO VAZIO \033[0m")
        while True:
            try:
                local_moradia = input('Onde mora: ')
                if local_moradia == "":
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! NÃO DEIXE O CAMPO VAZIO \033[0m")

        if heroi_ou_vilao == 1:
            alterego = input('Alterego: ')
            print('\n')
            return {'heroi_ou_vilao': heroi_ou_vilao, "nome": nome, "poder": poder, "fraqueza": fraqueza,
                    "empresa": empresa,
                    "local_moradia": local_moradia, "alterego": alterego}

        elif heroi_ou_vilao == 2:
            while True:
                try:
                    periculosidade = input('Periculosidade: ')
                    if periculosidade == "" or periculosidade < 0 or periculosidade > 1000:
                        raise ValueError
                    break
                except ValueError:
                    print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
            print('\n')
            return {'heroi_ou_vilao': heroi_ou_vilao, "nome": nome, "poder": poder, "fraqueza": fraqueza,
                    "empresa": empresa,
                    "local_moradia": local_moradia, "periculosidade": periculosidade}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_senciente(self, dados_senciente):
        if dados_senciente['codigo'] == 1:
            print('Nome do Super-Herói: ', dados_senciente['nome'])
            print('Fraqueza do Super-Herói: ', dados_senciente['fraqueza'])
            print('Empresa do Super-Herói: ', dados_senciente['empresa'])
            print('Local onde mora: ', dados_senciente['local_moradia'])
            if dados_senciente['alterego'] == "":
                print('Este Super-Herói não possui Alterego')
            else:
                print('Alterego do Super-Herói: ', dados_senciente['alterego'])
            print('\n')
        elif dados_senciente['codigo'] == 2:
            print('Nome do Vilão: ', dados_senciente['nome'])
            print('Fraqueza do Vilão: ', dados_senciente['fraqueza'])
            print('Empresa do Vilão: ', dados_senciente['empresa'])
            print('Local onde mora: ', dados_senciente['local_moradia'])
            print('Periculosidade do Vilão: ', dados_senciente['periculosidade'])
            print('\n')
        print('\n')

    def mostra_lista_super_herois(self, super_herois):
        print('----- Lista de Super-Heróis -----')
        for super_heroi in super_herois:
            print('Nome do Super-Herói: ', super_heroi.nome)
            print('Fraqueza do Super-Herói: ', super_heroi.fraqueza)
            print('Empresa do Super-Herói: ', super_heroi.empresa)
            print('Local onde mora: ', super_heroi.local_moradia)
            print('Alterego do Super-Herói: ', super_heroi.alterego)
            print('\n')

    def mostra_lista_viloes(self, viloes):
        print('----- Lista de Vilões -----')
        for vilao in viloes:
            print('Nome do Vilão: ', vilao.nome)
            print('Fraqueza do Vilão: ', vilao.fraqueza)
            print('Empresa do Vilão: ', vilao.empresa)
            print('Local onde mora: ', vilao.local_moradia)
            print('Periculosidade do Vilão: ', vilao.periculosidade)
            print('\n')

    def seleciona_senciente(self):
        nome = input('Nome do senciente (Super-Herói ou Vilão) que deseja selecionar: ')
        print('\n')
        return nome

    def seleciona_super_heroi(self):
        nome = input('Nome do Super-Herói que deseja selecionar: ')
        print('\n')
        return nome

    def seleciona_vilao(self):
        nome = input('Nome do Vilão que deseja selecionar: ')
        print('\n')
        return nome

    def mostra_mensagem(self, mensagem):
        print(mensagem)
