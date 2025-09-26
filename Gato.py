from Animal import Animal
class Gato(Animal):

    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self._cor = cor

    def fazer_som(self):
        return f'{self._nome} mia: Miau'

    def arranha_sofa(self):
        return f'{self._nome} esta arranhando o sofa'

