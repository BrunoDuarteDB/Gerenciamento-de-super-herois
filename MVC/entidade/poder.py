class Poder:
    def __init__(self, velocidade: int, forca: int, poder_magico: int, resistencia: int, inteligencia: int,
                 artes_marciais: int,
                 fator_cura: int, expertise: int, controle_natureza: int, detentor, media_poder: int):
        '''from MVC.entidade.vilao import Vilao
        if isinstance(detentor, Vilao):'''
        self.__detentor = detentor
        self.__velocidade = velocidade
        self.__forca = forca
        self.__poder_magico = poder_magico
        self.__resistencia = resistencia
        self.__inteligencia = inteligencia
        self.__artes_marciais = artes_marciais
        self.__fator_cura = fator_cura
        self.__expertise = expertise
        self.__controle_natureza = controle_natureza
        self.__media_poder = media_poder

    # Criar getter e setter para detentor? Sim *ERA ISSO *

    @property
    def detentor(self):
        return self.__detentor

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def forca(self):
        return self.__forca

    @property
    def poder_magico(self):
        return self.__poder_magico

    @property
    def resistencia(self):
        return self.__resistencia

    @property
    def inteligencia(self):
        return self.__inteligencia

    @property
    def artes_marciais(self):
        return self.__artes_marciais

    @property
    def fator_cura(self):
        return self.__fator_cura

    @property
    def expertise(self):
        return self.__expertise

    @property
    def controle_natureza(self):
        return self.__controle_natureza

    @property
    def media_poder(self):
        return self.__media_poder

    @detentor.setter
    def detentor(self, detentor):
         self.__detentor= detentor

    @velocidade.setter
    def velocidade(self, velocidade: int):
        self.__velocidade = velocidade

    @forca.setter
    def forca(self, forca: int):
        self.__forca = forca

    @poder_magico.setter
    def poder_magico(self, poder_magico: int):
        self.__poder_magico = poder_magico

    @resistencia.setter
    def resistencia(self, resistencia: int):
        self.__resistencia = resistencia

    @inteligencia.setter
    def inteligencia(self, inteligencia: int):
        self.__inteligencia = inteligencia

    @artes_marciais.setter
    def artes_marciais(self, artes_marciais: int):
        self.__artes_marciais = artes_marciais

    @fator_cura.setter
    def fator_cura(self, fator_cura: int):
        self.__fator_cura = fator_cura

    @expertise.setter
    def expertise(self, expertise: int):
        self.__expertise = expertise

    @controle_natureza.setter
    def controle_natureza(self, controle_natureza: int):
        self.__controle_natureza = controle_natureza

    @media_poder.setter
    def media_poder(self, media_poder: int):
        self.__media_poder = media_poder

