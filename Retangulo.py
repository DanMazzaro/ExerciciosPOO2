from Forma import Forma
class Retangulo(Forma):

    def __init__(self, nome, largura, altura):
        super().__init__(nome)
        self._largura = largura
        self._altura = altura

    def calcular_area(self):
        return f'a area do {self._nome} e: {self._largura * self._altura}'

