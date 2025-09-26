from Forma import Forma
class Circulo(Forma):

    def __init__(self, nome, raio):
        super().__init__(nome)
        self._raio = raio

    def calcular_area(self):
        return f'a area do  e: {3.14159 * (raio * raio)}'

