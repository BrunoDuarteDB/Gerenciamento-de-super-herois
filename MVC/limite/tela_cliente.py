

class TelaCliente():

    def __init__(self, controlador_cliente):
        self.__controlador_cliente = controlador_cliente

    def tela_opcoes(self):
        print("-------- CLIENTES ----------")
        print("Escolha a opção: ")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        nome = input("Titulo: ")
        pais_origem = input("País de Origem: ")
        local_sede = input("Local da Sede: ")
        codigo= input("Código: ")

        return {"nome": nome, "pais_origem": pais_origem, "local_sede": local_sede, "codigo": codigo}

        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def mostra_cliente(self, dados_cliente):
        print("------ CLIENTE ------")
        print("NOME DO CLIENTE: ", dados_cliente["nome"])
        print("PAÍS DE ORIGEM DO CLIENTE: ", dados_cliente["pais_origem"])
        print("LOCAL DA SEDE DO CLIENTE: ", dados_cliente["local_sede"])
        print("CÓDIGO DO CLIENTE: ", dados_cliente['codigo'])
        print("\n")

    def mostra_lista_clientes(self, clientes):
        print("------ LISTA DE CLIENTES ------")
        for cliente in clientes:
            print("NOME DO CLIENTE: ", cliente.nome)
            print("PAÍS DE ORIGEM DO CLIENTE: ", cliente.pais_origem)
            print("LOCAL DA SEDE DO CLIENTE: ", cliente.local_sede)
            print("CÓDIGO DO CLIENTE: ", cliente.codigo)
            print("\n")

        # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado

    def seleciona_cliente(self):
        codigo = input("Codigo do cliente que deseja selecionar: ")
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
