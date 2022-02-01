class TelaPoder:
    # Fazer tratamento de erros
    def tela_opcoes(self):
        print("-------- PODER --------")
        print("Escolha a opção")
        print("1- Incluir poder")
        print("2- Alterar poder")
        print("3- Listar poderes")
        print("4- Excluir poder")
        print("5- Mostrar a o valor médio de poder")
        print("0- Retornar")

        return int(input("Escolha a opção: "))

    def pega_dados_poder(self):
        print("-------- DADOS PODER --------")
        detentor= input("Detentor: ")
        velocidade = input("Velocidade: ")
        forca = input("Força: ")
        poder_magico = input("Poder Mágico: ")
        resistencia = input("Resistência: ")
        inteligencia = input("Inteligência: ")
        artes_marciais = input("Artes Marciais: ")
        fator_cura = input("Fator Cura: ")
        expertise = input("Expertise: ")
        controle_natureza = input("Controle da Natureza: ")

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
        print("\n")

    def seleciona_poder(self):
        detentor = input("Nome do detentor do poder que deseja selecionar: ")
        return detentor

    def mostra_mensagem(self, msg):
        print(msg)
