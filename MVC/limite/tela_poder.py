class TelaPoder():

    def __init__(self, controlador_poder):
        self.__controlador_poder = controlador_poder

    def tela_opcoes(self):
        print("-------- PODER --------")
        print("Escolha a opção")
        print("1 - Incluir poder")
        print("2 - Alterar poder")
        print("3 - Listar poderes")
        print("4 - Excluir poder")
        print("5 - Mostrar o valor médio de poder")
        print("0 - Retornar")

        while True:
            try:
                opcoes_validas = [0, 1, 2, 3, 4, 5]
                opcao = int(input("Escolha a opção: "))
                print('\n')
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("\033[1;31mOPÇÃO INVÁLIDA! \033[0m")
                print('\n')

    def pega_dados_poder(self, nome=None):

        print("-------- DADOS PODER --------")
        print("\033[1;32mPara poderes, digite um valor de 0 a 1000. \033[0m")
        if nome is None:
            while True:
                try:
                    detentor = input("Detentor: ").strip()
                    if detentor == "":
                        raise ValueError
                    break
                except ValueError:
                    print("\033[1;31mATENÇÃO! NÃO DEIXE O CAMPO VAZIO \033[0m")
        elif nome is not None:
            detentor = nome
        while True:
            try:
                velocidade = int(input("Velocidade: "))
                if velocidade == "" or velocidade< 0 or velocidade>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        while True:
            try:
                forca = int(input("Força: "))
                if forca == "" or forca< 0 or forca>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        while True:
            try:
                poder_magico = int(input("Poder Mágico: "))
                if poder_magico == "" or poder_magico< 0 or poder_magico>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        while True:
            try:
                resistencia = int(input("Resistência: "))
                if resistencia == "" or resistencia< 0 or resistencia>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        while True:
            try:
                inteligencia = int(input("Inteligência: "))
                if inteligencia == "" or inteligencia< 0 or inteligencia>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        while True:
            try:
                artes_marciais = int(input("Artes Marciais: "))
                if artes_marciais == "" or artes_marciais< 0 or artes_marciais>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        while True:
            try:
                fator_cura = int(input("Fator Cura: "))
                if fator_cura == "" or fator_cura< 0 or fator_cura>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        while True:
            try:
                expertise = int(input("Expertise: "))
                if expertise == "" or expertise< 0 or expertise>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        while True:
            try:
                controle_natureza = int(input("Controle da Natureza: "))
                if controle_natureza == "" or controle_natureza< 0 or controle_natureza>1000:
                    raise ValueError
                break
            except ValueError:
                print("\033[1;31mATENÇÃO! DIGITE UM NÚMERO VÁLIDO \033[0m")
        print('\n')
        return {"detentor": detentor, "velocidade": velocidade, "forca": forca, "poder_magico": poder_magico,
                "resistencia": resistencia,
                "inteligencia": inteligencia, "artes_marciais": artes_marciais, "fator_cura": fator_cura,
                "expertise": expertise,
                "controle_natureza": controle_natureza}

    def mostra_poder(self, dados_poder):
        print(f"\033[1;32mPoder de {dados_poder['detentor'] } \033[0m")
        print("DETENTOR: ", dados_poder["detentor"])
        print("VELOCIDADE: ", dados_poder["velocidade"])
        print("FORÇA: ", dados_poder["forca"])
        print("PODER MÁGICO: ", dados_poder["poder_magico"])
        print("RESISTÊNCIA: ", dados_poder["resistencia"])
        print("INTELIGÊNCIA: ", dados_poder["inteligencia"])
        print("ARTES MARCIAIS: ", dados_poder["artes_marciais"])
        print("FATOR CURA: ", dados_poder["fator_cura"])
        print("EXPERTISE: ", dados_poder["expertise"])
        print("CONTROLE DA NATUREZA: ", dados_poder["controle_natureza"])
        print("\n")

    def seleciona_poder(self):
        detentor = input("Nome do detentor do poder que deseja selecionar: ")
        print('\n')
        return detentor

    def mostra_mensagem(self, msg):
        print(msg)
        print("\n")
