class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def apresentar(self):
        return f'ola, meu nome é {self._nome} e tenho {self._idade} anos'
    
    def fazer_som(self):
        return f'{self._nome} faz um som'
    