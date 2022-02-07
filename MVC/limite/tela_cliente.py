class TelaCliente():

    def __init__(self, controlador_cliente):
        self.__controlador_cliente = controlador_cliente

    def tela_opcoes(self):
        print("\033[1;93m-------- CLIENTES ----------\033[0m")
        print("Escolha a opção: ")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        while True:
            try:
                opcoes_validas = [0, 1, 2, 3, 4]
                opcao = int(input("Escolha a opção: "))
                print()
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("\033[1;31mOPÇÃO INVÁLIDA! \033[0m")
                print()

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        while True:
            try:
                nome = input("Título: ").strip()
                if nome == "" or nome.isdigit() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO. \033[0m")
        while True:
            try:
                pais_origem = input("País de Origem: ")
                if pais_origem == "" or pais_origem.isdigit() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO.  \033[0m")
        while True:
            try:
                local_sede = input("Local da Sede: ")
                if local_sede == "" or local_sede.isdigit() is True:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! VALOR INVÁLIDO.  \033[0m")
        while True:
            try:
                codigo = input("Código: ")
                if codigo.isnumeric() is False:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mCÓDIGO INVÁLIDO! DIGITE UM NÚMERO INTEIRO \033[0m")

        print()

        return {"nome": nome, "pais_origem": pais_origem, "local_sede": local_sede, "codigo": codigo}

    def mostra_cliente(self, dados_cliente):
        print("------ CLIENTE ------")
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("PAÍS DE ORIGEM DO CLIENTE: ", dados_cliente["pais_origem"])
        print("LOCAL DA SEDE DO CLIENTE: ", dados_cliente["local_sede"])
        print("CÓDIGO DO CLIENTE: ", dados_cliente['codigo'])
        print()

    def mostra_lista_clientes(self, clientes):
        print("------ LISTA DE CLIENTES ------")
        for cliente in clientes:
            print("NOME DO CLIENTE: ", cliente.nome)
            print("PAÍS DE ORIGEM DO CLIENTE: ", cliente.pais_origem)
            print("LOCAL DA SEDE DO CLIENTE: ", cliente.local_sede)
            print("CÓDIGO DO CLIENTE: ", cliente.codigo)
            print()

    def seleciona_cliente(self):
        codigos = []
        for cliente in self.__controlador_cliente.clientes:
            codigos.append(cliente.codigo)
        while True:
            try:
                codigo = input("Código do cliente que deseja selecionar: ")
                if codigo.isnumeric() is False or codigo not in codigos:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! ESSE CÓDIGO DE CLIENTE NÃO EXISTE! \033[0m")
        print()
        return codigo

    def deseja_mais(self):
        while True:
            try:
                pergunta = input('Deseja adicionar mais um cliente? (S/N): ')
                if pergunta not in {"S", "s", "N", "n"}:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mRESPOSTA INVÁLIDA. DIGITE S OU N \033[0m")
        print()
        return pergunta

    def mostra_mensagem(self, msg):
        print(msg)
