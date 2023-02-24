
import psycopg2
from Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
from Modelo.classCarros import Carros
from Modelo.classAluguel import Aluguel

def verClientes(conexao):
        clientes = conexao.consultarBanco('''
        SELECT * FROM "Clientes"
        ''')
        print("ID | Nome Cliente | Cpf Cliente")
        for cliente in clientes:
            print(f"{cliente[0]} | {cliente[1]} | {cliente[3]}")

    
def verCarros(conexao):
        carros = conexao.consultarBanco('''
        SELECT * FROM "Carros"
        ''')
        print("ID Carro | Modelo Carro | Fabricante Carro | Ano do Carro")
        for carro in carros:
            print(f"{carro[0]} | {carro[2]} | {carro[4]} | {carro[5]} | {carro[6]}")


def verAlugueis(conexao):

    alugueis = conexao.consultarBanco('''
    Select * FROM "Aluguel"
    ORDER BY "ID" ASC
    ''')
    print("ID Aluguel | Nome Cliente | Modelo Carro | Data de Aluguel")

    for aluguel in alugueis:

        nomeDoCliente = conexao.consultarBanco(f'''
        SELECT "Nome_Cliente" FROM "Clientes"
        WHERE "ID_Cliente" = {aluguel[1]}
        ''')[0][0]

        modeloCarro = conexao.consultarBanco(f'''
        SELECT "Modelo_Carro" FROM "Carros"
        WHERE "ID_Carro" = {aluguel[2]}
        ''')[0][0]
        
        print(f'{aluguel[0]} | {nomeDoCliente} | {modeloCarro} | {aluguel[3]}')

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
                    verCarros(con)
                    
                case "2":
                    Carros.InserirCarro(conexao)
            
                case "3":
                    Carros.removerCarro(conexao)
                
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
                    verAlugueis(con)
                    
                case "2":
                    Aluguel.inserirAluguel(conexao)
            
                case "3":
                    Aluguel.removerAluguel(conexao)

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
                    verClientes(con)
                    
                case "2":
                    Cliente.cadastrarCliente(conexao)
            
                case "3":
                    Cliente.editarCliente(conexao)
                
                case "4":
                    Cliente.removerCliente(conexao)

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
        [3] Alugueis
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
                break
            case _:
                print("Você escolheu uma opção inválida!\n")

        input("Tecle Enter para continuar.")
    con.fechar()


except(Exception, psycopg2.Error) as error:
    print("Ocorreu um erro", error)
