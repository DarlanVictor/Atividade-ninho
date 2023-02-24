from Controle.classConexao import Conexao

class Cliente:

    def __init__(self, ID, Nome, Cpf, Telefone, Endereco, Data_nascimento):
        self._ID = ID
        self._Nome = Nome
        self._Cpf = Cpf
        self._Telefone = Telefone
        self._Endereco = Endereco
        self._Data_nascimento = Data_nascimento

    def listarClientesId(self):
        sql = '''
        SELECT * FROM "Clientes"
        ORDER BY "ID_Cliente" ASC
        '''
        clientes = Conexao.consultarBanco(sql)
        print("ID | Nome")
        for cliente in clientes:
            print(f"{cliente[0]} | {cliente[1]}")
        return sql

    def cadastrarCliente(self):
        nomeCliente = input('Digite o nome do Cliente: ')
        cpfCliente = input('Digite o cpf do Cliente: ')
        telefoneCliente = input('Digite o telefone do Cliente: ')
        enderecoCliente = input('Digite o endereço do Cliente: ')
        dataNascimentoCliente = input('Digite a data de nascimento do Cliente: ')
        sql = f'''
        INSERT INTO "Clientes"
        VALUES(Default, '{nomeCliente}', '{cpfCliente}', '{telefoneCliente}', '{enderecoCliente}', '{dataNascimentoCliente}')
        '''
        print('Cliente cadastrado com sucesso!')
        return sql

    
    def editarCliente(self):
        self.listarClientesId()
        idCliente = int(input("Digite o id do cliente que deseja alterar?: "))
        sql = f'''
        SELECT * FROM "Clientes"
        WHERE "ID_Cliente" = {idCliente}
        '''
        print(f"Alterando...")
        novoNome = input("Digite o novo Nome: ")
        novoCpf = input("Digite o novo Cpf: ")
        novoTelefone = input("Digite o novo Telefone: ")
        novoEndereco = input("Digite o novo Endereço: ")
        novaData_nascimento = input("Digite a nova data de nascimento: ")
        sql = f'''
        UPDATE "Clientes"
        SET "Nome_Cliente" = '{novoNome}', "CPF_Cliente" = '{novoCpf}', "Telefone_Cliente" = '{novoTelefone}', "Endereco_Cliente" = '{novoEndereco}', "Data_nascimento_Cliente" = '{novaData_nascimento}'
        WHERE "ID_Cliente" = {idCliente}
        '''
        Conexao().manipularBanco(sql)
        print('Cliente alterado com sucesso!')
        return sql

    def removerCliente(self):
        self.listarClientesId()
        idCliente = int(input("Digite o Id do cliente que deseja remover?: "))
        sql = f'''
        SELECT * FROM "Clientes"
        WHERE "ID_Cliente" = {idCliente}
        '''
        Conexao().manipularBanco(sql)
        sql = f'''
        DELETE FROM "Clientes"
        WHERE "ID_Cliente" = {idCliente}
        '''
        Conexao().manipularBanco(sql)
        print('Cliente removido com sucesso!')
        return sql
    