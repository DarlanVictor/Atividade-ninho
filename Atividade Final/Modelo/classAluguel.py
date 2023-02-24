from Controle.classConexao import Conexao

class Aluguel:
    def __init__(self, ID_Aluguel, ID_Cliente, ID_Carro, Data_Aluguel, Data_Devolucao, Local_LugCar, Valor_Total):
        self._ID_Aluguel = ID_Aluguel
        self._ID_Cliente = ID_Cliente
        self._ID_Carro = ID_Carro
        self._Data_Aluguel = Data_Aluguel 
        self._Data_Devolucao = Data_Devolucao
        self._Local_LugCar = Local_LugCar
        self._Valor_Total = Valor_Total

    def exibirCliente(self):
        sql = '''
        SELECT ID_Cliente, Nome_Cliente FROM "Clientes"
        '''
        clientes = Conexao.consultarBanco(sql)
        for cliente in clientes:
            print(f"{cliente[0]} | {cliente[1]}")
        return sql
    
    def exibirCarro(self):
        sql = '''
        SELECT ID_Carro, Modelo_Carro FROM "Carros"
        '''
        carros = Conexao.consultarBanco(sql)
        for carro in carros:
            print(f"{carro[0]} | {carro[2]}")
        return sql

    def inserirAluguel(self):
        self.exibirCliente()
        self.exibirCarro()
        idcliente = input('Digite o ID do Cliente: ')
        idcarro = input('Digite o ID do Carro: ')
        dataAluguel = input('Digite a data do aluguel: ')
        dataDevolucao = input('Digite a data de devolução do carro: ')
        localLugCar = "BR222 km6 8000"
        sql = f'''
        INSERT INTO "Aluguel"
        VALUES(default, '{idcliente}', '{idcarro}', '{dataAluguel}', '{dataDevolucao}', '{localLugCar}')
        '''
        print('Carro alugado com sucesso!')
        return sql

    def removerAluguel(self):
        
        IdAluguel = int(input("Digite o Id do aluguel que deseja remover?: "))
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID_Aluguel" = {self._ID_Aluguel}
        '''
        sql = f'''
        DELETE FROM "Carros"
        WHERE "ID_carro" = {IdAluguel}
        '''
        print('Aluguel removido com sucesso!')
        return sql