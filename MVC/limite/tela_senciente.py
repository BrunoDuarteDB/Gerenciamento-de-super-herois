class TelaSenciente():

    def __init__(self, controlador_senciente):
        self.__controlador_senciente = controlador_senciente

    def tela_opcoes(self):
        print('\033[1;96m---------- SENCIENTE ----------\033[0m')
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
                print()
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print('Opção inválida!')
                print()

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
                if nome == "" or nome.isdigit() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO. \033[0m")
        poder = self.__controlador_senciente.pede_cadastro_poder(nome)
        while True:
            try:
                fraqueza = input('Fraqueza ("kryptonita, por exemplo"): ')
                if fraqueza.isdigit() is True or fraqueza == "":
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO \033[0m")
        while True:
            try:
                empresa = input('Empresa: ')
                if empresa.isdigit() is True or empresa == "":
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO \033[0m")
        while True:
            try:
                local_moradia = input('Onde mora: ')
                if local_moradia == "" or local_moradia.isdigit() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO \033[0m")

        if heroi_ou_vilao == 1:
            while True:
                try:
                    alterego = input('Alter ego: ')
                    if alterego == "" or alterego.isdigit() is True:
                        raise ValueError
                    break
                except ValueError:
                    print("\033[1;31mATENÇÃO! VALOR INVÁLIDO \033[0m")
            print()
            return {'heroi_ou_vilao': heroi_ou_vilao, "nome": nome, "poder": poder, "fraqueza": fraqueza,
                    "empresa": empresa,
                    "local_moradia": local_moradia, "alterego": alterego}

        elif heroi_ou_vilao == 2:
            while True:
                try:
                    periculosidade = int(input('Periculosidade: '))
                    if periculosidade == "" or periculosidade < 0 or periculosidade > 1000:
                        raise ValueError
                    break
                except ValueError:
                    print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
            print()
            return {'heroi_ou_vilao': heroi_ou_vilao, "nome": nome, "poder": poder, "fraqueza": fraqueza,
                    "empresa": empresa,
                    "local_moradia": local_moradia, "periculosidade": periculosidade}

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
            print()
        elif dados_senciente['codigo'] == 2:
            print('Nome do Vilão: ', dados_senciente['nome'])
            print('Fraqueza do Vilão: ', dados_senciente['fraqueza'])
            print('Empresa do Vilão: ', dados_senciente['empresa'])
            print('Local onde mora: ', dados_senciente['local_moradia'])
            print('Periculosidade do Vilão: ', dados_senciente['periculosidade'])
            print()
        print()

    def mostra_lista_super_herois(self, super_herois):
        print('----- Lista de Super-Heróis -----')
        for super_heroi in super_herois:
            print('Nome do Super-Herói: ', super_heroi.nome)
            print('Fraqueza do Super-Herói: ', super_heroi.fraqueza)
            print('Empresa do Super-Herói: ', super_heroi.empresa)
            print('Local onde mora: ', super_heroi.local_moradia)
            print('Alterego do Super-Herói: ', super_heroi.alterego)
            print()

    def mostra_lista_viloes(self, viloes):
        print('----- Lista de Vilões -----')
        for vilao in viloes:
            print('Nome do Vilão: ', vilao.nome)
            print('Fraqueza do Vilão: ', vilao.fraqueza)
            print('Empresa do Vilão: ', vilao.empresa)
            print('Local onde mora: ', vilao.local_moradia)
            print('Periculosidade do Vilão: ', vilao.periculosidade)
            print()

    def seleciona_senciente(self):
        nomes_sencientes = []
        for super_heroi in self.__controlador_senciente.super_herois:
            nomes_sencientes.append(super_heroi.nome)
        for vilao in self.__controlador_senciente.viloes:
            nomes_sencientes.append(vilao.nome)
        while True:
            try:
                nome = input('Nome do senciente (Super-Herói ou Vilão) que deseja selecionar: ')
                if nome.isdigit() is True or nome not in nomes_sencientes:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! ESSE NOME DE SENCIENTE NÃO EXISTE! \033[0m")
        print()
        return nome

    def seleciona_super_heroi(self):
        nomes_super_herois = []
        for super_heroi in self.__controlador_senciente.super_herois:
            nomes_super_herois.append(super_heroi.nome)
        while True:
            try:
                nome = input('Nome do Super-Herói que deseja selecionar: ')
                if nome.isdigit() is True or nome not in nomes_super_herois:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! ESSE NOME DE SUPER-HERÓI NÃO EXISTE! \033[0m")
        print()
        return nome

    def seleciona_vilao(self):
        nomes_viloes = []
        for vilao in self.__controlador_senciente.viloes:
            nomes_viloes.append(vilao.nome)
        while True:
            try:
                nome = input('Nome do Vilão que deseja selecionar: ')
                if nome.isdigit() is True or nome not in nomes_viloes:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! ESSE NOME DE VILÃO NÃO EXISTE! \033[0m")
        print()
        return nome

    def mostra_mensagem(self, mensagem):
        print(mensagem)
