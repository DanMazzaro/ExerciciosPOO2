from Funcionario import Funcionario
class Desenvolvedor(Funcionario):

    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self._linguagem = linguagem

    def exibir_detalhes(self):
        return f'nome: {nome}, salario: R${salario}, linguagem: {linguagem}'

    def calcular_bonus(self):
        return f' o bonus do salario é {salario * 0.12}'
