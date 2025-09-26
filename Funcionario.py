class Funcionario:

    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def exibir_detalhes(self):
        return f'nome: {nome}, salario: R${salario}'

    def calcular_bonus(self):
        return f'o bonus é de {salario * 0.10}'