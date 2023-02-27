def verClientes(conexao):
        clientes = conexao.consultarBanco('''
        SELECT * FROM "Clientes"
        ''')
        print("ID | Nome Cliente | Cpf Cliente")
        for cliente in clientes:
            print(f"{cliente[0]} | {cliente[1]} | {cliente[2]}")

def cadastrarCliente(conexao):
        nomeCliente = input('Digite o nome do Cliente: ')
        cpfCliente = input('Digite o cpf do Cliente: ')
        telefoneCliente = input('Digite o telefone do Cliente: ')
        enderecoCliente = input('Digite o endereço do Cliente: ')
        dataNascimentoCliente = input('Digite a data de nascimento do Cliente: ')
        conexao.manipularBanco(f'''
        INSERT INTO "Clientes"
        VALUES(Default, '{nomeCliente}', '{cpfCliente}', '{telefoneCliente}', '{enderecoCliente}', '{dataNascimentoCliente}')
        ''')
        print('Cliente cadastrado com sucesso!')

def removerCliente(conexao):
        verClientes(conexao)
        idCliente = int(input("Digite o Id do cliente que deseja remover?: "))
        conexao.manipularBanco(f'''
        DELETE FROM "Clientes"
        WHERE "ID_Cliente" = {idCliente}
        ''')
        
        print('Cliente removido com sucesso!')

def editarCliente(conexao):
        verClientes(conexao)
        idCliente = int(input("Digite o id do cliente que deseja alterar?: "))
        conexao.manipularBanco(f'''
        SELECT * FROM "Clientes"
        WHERE "ID_Cliente" = {idCliente}
        ''')
        print(f"Alterando...")
        novoNome = input("Digite o novo Nome: ")
        novoCpf = input("Digite o novo Cpf: ")
        novoTelefone = input("Digite o novo Telefone: ")
        novoEndereco = input("Digite o novo Endereço: ")
        novaData_nascimento = input("Digite a nova data de nascimento: ")
        conexao.manipularBanco(f'''
        UPDATE "Clientes"
        SET "Nome_Cliente" = '{novoNome}', "CPF_Cliente" = '{novoCpf}', "Telefone_Cliente" = '{novoTelefone}', "Endereco_Cliente" = '{novoEndereco}', "Data_nascimento_Cliente" = '{novaData_nascimento}'
        WHERE "ID_Cliente" = {idCliente}
        ''')
        
        print('Cliente alterado com sucesso!')      
        

def verCarros(conexao):
        carros = conexao.consultarBanco('''
        SELECT * FROM "Carros"
        ''')
        print("ID Carro | Modelo Carro | Fabricante Carro | Ano do Carro | Diária do Carro")
        for carro in carros:
            print(f"{carro[0]} | {carro[2]} | {carro[4]} | {carro[5]} | {carro[6]}")

def InserirCarro(conexao):
        placaCarro = input("Qual a placa do carro: ")
        modeloCarro = input("Qual o modelo do carro: ")
        descricaoCarro = input("Qual a descricao do carro: ")
        fabricanteCarro = input("Qual o fabricante do carro: ")
        anoCarro = input("Qual o ano de fabricação do carro: ")
        diariaCarro = input("Quanto é a diária do carro: ")
        conexao.manipularBanco(f'''
        INSERT INTO "Carros"
        VALUES(default, '{placaCarro}', '{modeloCarro}', '{descricaoCarro}', '{fabricanteCarro}', '{anoCarro}', '{diariaCarro}')
        ''')
        print('Carro inserido com sucesso!')

def removerCarro(conexao):
        verCarros(conexao)
        
        Idcarro = int(input("Digite o Id do carro que deseja remover?: "))
        conexao.manipularBanco(f'''
        DELETE FROM "Carros"
        WHERE "ID_Carro" = {Idcarro}
        ''')
        print('Carro removido com sucesso!')


def verAlugueis(conexao):

    alugueis = conexao.consultarBanco('''
    Select * FROM "Aluguel"
    ORDER BY "ID_Aluguel" ASC
    ''')
    print("ID Aluguel | Nome Cliente | Modelo Carro | Data do Aluguel | Data de Devolução")

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

def inserirAluguel(conexao):
        verClientes(conexao)
        verCarros(conexao)
        idcliente = input('Digite o ID do Cliente: ')
        idcarro = input('Digite o ID do Carro: ')
        dataAluguel = input('Digite a data do aluguel: ')
        dataDevolucao = input('Digite a data de devolução do carro: ')
        localLugCar = "BR222 km6 8000"
        conexao.manipularBanco(f'''
        INSERT INTO "Aluguel"
        VALUES(default, '{idcliente}', '{idcarro}', '{dataAluguel}', '{dataDevolucao}', '{localLugCar}')
        ''')
        print('Carro alugado com sucesso!')

def removerAluguel(conexao):
        verAlugueis(conexao)
        
        IdAluguel = int(input("Digite o Id do aluguel que deseja remover?: "))
        conexao.manipularBanco(f'''
        DELETE FROM "Aluguel"
        WHERE "ID_Aluguel" = {IdAluguel}
        ''')
        print('Aluguel removido com sucesso!')
