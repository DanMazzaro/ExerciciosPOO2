from Funcionario import Funcionario
class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self._departamento = departamento

    def exibir_detalhes(self):
        return f'nome: {nome}, salario: R${salario}, departamento: {departamento}'

    def calcular_bonus(self):
        return f' o bonus do salario é {salario * 0.15}'

    