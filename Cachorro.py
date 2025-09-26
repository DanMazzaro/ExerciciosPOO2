from Animal import Animal

class Cachorro(Animal):

    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self._raca = raca

    def fazer_som(self):
        return f'{self._nome} late: Au Au'
    
    def buscar_bolinha(self):
        return f'{self._nome} esta buscando a bolinha'
    

