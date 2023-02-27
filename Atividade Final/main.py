import psycopg2
from Controle.classConexao import Conexao
from funçoes import *


def menuCarros(conexao):
        while True:
        
            
            print(f'''
            Escolha uma das opções:
            [1] Ver Carros
            [2] Inserir Carro
            [3] Remover Carro
            [0] Voltar para o menu principal
            ''')
            opcoes = input("Digite o número da opção desejada: ")
            match opcoes:
                
                case "1":
                    verCarros(conexao)
                    
                case "2":
                    InserirCarro(conexao)
            
                case "3":
                    removerCarro(conexao)
                
                case "0":
                    print("Voltando para o menu principal")
                    break

                case _:
                    print("Você digitou uma opção inválida")


def menuAluguel(conexao):
        while True:
        
            
            print(f'''
            Escolha uma das opções:
            [1] Ver Alugueis
            [2] Inserir Aluguel
            [3] Remover Aluguel
            [0] Voltar para o menu principal
            ''')
            opcoes = input("Digite o número da opção desejada: ")
            match opcoes:
                
                case "1":
                    verAlugueis(conexao)
                    
                case "2":
                    inserirAluguel(conexao)
            
                case "3":
                    removerAluguel(conexao)

                case "0":
                    print("Voltando para o menu principal")
                    break

                case _:
                    print("Você digitou uma opção inválida")


def menuClientes(conexao):
        while True:
        
            
            print(f'''
            Escolha uma das opções:
            [1] Ver clientes
            [2] Cadastrar Cliente
            [3] Editar Cliente
            [4] Remover Cliente
            [0] Voltar para o menu principal
            ''')
            opcoes = input("Digite o número da opção desejada: ")
            match opcoes:
                
                case "1":
                    verClientes(conexao)
                    
                case "2":
                    cadastrarCliente(conexao)
            
                case "3":
                    editarCliente(conexao)
                
                case "4":
                    removerCliente(conexao)

                case "0":
                    print("Voltando para o menu principal")
                    break

                case _:
                    print("Você digitou uma opção inválida")


try:

    con = Conexao("LugCar","localhost","5432","postgres","postgres")

    while True:

        print('''Bem vindo a locadora de carros populares LUGCAR
        
        Menu:
        [1] Clientes
        [2] Carros
        [3] Alugar Carros
        [0] Sair
        
        ''')

        opcoes = input("Digite a opção escolhida: ")

        match opcoes:
            case "1":
                menuClientes(con)
            case "2":
                menuCarros(con)
            case "3":
                menuAluguel(con)
            case "0":
                print('Finalizando aplicação...')
                break
            case _:
                print("Você escolheu uma opção inválida!\n")

        input("Tecle Enter para continuar.")
    con.fechar()


except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro", error)
