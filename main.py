from Cachorro import Cachorro
from Gato import Gato
from Retangulo import Retangulo
from Circulo import Circulo
from Gerente import Gerente
from Desenvolvedor import Desenvolvedor

print('menu de atividade:\natividade 1 Animal\natividade 2 Forma\n atividade 3 Funcionario')
atividade = input('digite 1, 2 ou 3 para escolher a atividade')

while True:

    if atividade == '1':

        opcao = input('digite 1 para dar um nome ao cachorro, digite 2 para dar um nome ao gato, digite qualquer coisa para sair: ')

        while True:

            if opcao == '1':
                nome = str(input('digite o nome do cachorro: '))
                idade = int(input('digite a idade do cachorro: '))
                raca = ('qual a raça do cachorro: ')

                cachorro = Cachorro(nome, idade, raca)

                print(cachorro.fazer_som())
                print(cachorro.buscar_bolinha())

                opcao = input('digite 1 para dar um nome ao cachorro, digite 2 para dar um nome ao gato: ')

            elif opcao == '2':
                nome = str(input('digite o nome do gato: '))
                idade = int(input('digite a idade do gato: '))
                cor = ('qual a cor do gato: ')

                gato = Gato(nome, idade, cor)

                print(gato.fazer_som())
                print(gato.arranha_sofa())

                opcao = input('digite 1 para dar um nome ao cachorro, digite 2 para dar um nome ao gato')

            else:
                print('voce nao digitou 1 ou 2')
                break

        atividade = input('digite 1, 2 ou 3 para escolher a atividade')

    elif atividade == '2':
        
        while True:
            opcao = input('digite 1 para calcular a area do retangulo, digite 2 para calcular a area do circulo: ')

            if opcao == '1':

                nome = ('retangulo')
                largura = float(input('digite a largura do retangulo: '))
                altura = float(input('digite a altura do retangulo: '))

                retangulo = Retangulo(nome, largura, altura)

                print(retangulo.calcular_area())

            elif opcao == '2':
                
                nome = ('circulo')
                raio = float(input('digite o raio do circulo: '))

                circulo = Circulo(nome, raio)

                print(circulo.calcular_area())

            else:
                print('voce saiu')
                break

        atividade = input('digite 1, 2 ou 3 para escolher a atividade')

    elif atividade == '3':

        opcao = input('digite 1 para abrir a classe Gerente e 2 para abrir a classe Desenvolvedor: ')

        if opcao == '1':
            nome = str(input('digite o nome do gerente:'))
            salario = float(input('digite o salario do gerente: ')) 
            departamento = input('digite o departamento do gerente: ')

            gerente = Gerente(nome, salario, departamento)

            print(gerente.exibir_detalhes())
            print(gerente.calcular_bonus())

        elif opcao == '2':
            nome = str(input('digite o nome do desenvolvedor:'))
            salario = float(input('digite o salario do desenvolvedor: ')) 
            linguagem = input('digite a linguagem do desenvolvedor: ')
                

            desenvolvedor = Desenvolvedor(nome, salario, linguagem)

            print(desenvolvedor.exibir_detalhes())
            print(desenvolvedor.calcular_bonus())

        else:
            print('voce saiu')
            break

        atividade = input('digite 1, 2 ou 3 para escolher a atividade')
        