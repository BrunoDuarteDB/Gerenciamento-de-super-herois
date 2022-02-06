

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
        print("5 - Mostrar a o valor médio de poder")
        print("0 - Retornar")

        while True:
            try:
                opcoes_validas=[0,1,2,3,4,5]
                opcao= int(input("Escolha a opção: "))
                print('\n')
                if opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("\033[1;31mOPÇÃO INVÁLIDA! \033[0m")
                print('\n')

    def pega_dados_poder(self):
        print("-------- DADOS PODER --------")
        detentor= input("Detentor: ")
        velocidade = int(input("Velocidade: "))
        forca = int(input("Força: "))
        poder_magico = int(input("Poder Mágico: "))
        resistencia = int(input("Resistência: "))
        inteligencia = int(input("Inteligência: "))
        artes_marciais = int(input("Artes Marciais: "))
        fator_cura = int(input("Fator Cura: "))
        expertise = int(input("Expertise: "))
        controle_natureza = int(input("Controle da Natureza: "))
        print('\n')

        return {"detentor": detentor, "velocidade": velocidade, "forca": forca, "poder_magico": poder_magico,
                "resistencia": resistencia,
                "inteligencia": inteligencia, "artes_marciais": artes_marciais, "fator_cura": fator_cura,
                "expertise": expertise,
                "controle_natureza": controle_natureza}

    def mostra_poder(self, dados_poder):
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

    def seleciona_poder(self):
        detentor = input("Nome do detentor do poder que deseja selecionar: ")
        print('\n')
        return detentor

    def mostra_mensagem(self, msg):
        print(msg)
