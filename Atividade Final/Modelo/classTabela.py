from Controle.classConexao import Conexao

class Tabela:
    def __init__(self):
        self.conexao = Conexao()

    def criarBancoDeDados(self):
        sql = '''
        DROP DATABASE IF EXISTS "LugCar" ;
        CREATE DATABASE "LugCar"
        '''
        self.conexao.manipularBanco(sql)

    def criarTabelaClientes(self):
        sql = '''
        DROP TABLE IF EXISTS "Clientes";
        CREATE TABLE "Clientes"(
            "ID_Cliente" int GENERATED ALWAYS AS IDENTITY,
            "Nome_Cliente" varchar(255) NOT NULL,
            "Cpf_Cliente" char(11) UNIQUE NOT NULL,
            "Telefone_Cliente" char(11),
            "Endereco_Cliente" varchar(100) NOT NULL,
            "Data_Nascimento" date,
            Primary Key("ID_Cliente")
        );
        '''
        self.conexao.manipularBanco(sql)

    def criarTabelaCarros(self):
        sql = '''
        DROP TABLE IF EXISTS "Carros";
        CREATE TABLE "Carros"(
            "ID_Carro" int GENERATED ALWAYS AS IDENTITY,
            "Placa_Carro" char(7) NOT NULL,
            "Modelo_Carro" varchar(100) NOT NULL,
            "Descricao_Carro" varchar(255),
            "Fabricante_Carro" varchar(100) NOT NULL,
            "Ano_Carro" int NOT NULL,
            "Diaria_Carro" money NOT NULL,
            Primary Key("ID_Carro")
        );
        '''
        self.conexao.manipularBanco(sql)

    def criarTabelaAlugueis(self):
        sql = '''
        DROP TABLE IF EXISTS "Aluguel";
        CREATE TABLE "Aluguel"(
            "ID_Aluguel" int GENERATED ALWAYS AS IDENTITY,
            "ID_Cliente" int,
            "ID_Carro" int,
            "Data_Aluguel" date NOT NULL,
            "Data_Devolucao" date NOT NULL,
            "Local_LugCar" varchar(150),
            "Valor_Total" money,
            Primary Key("ID_Aluguel"),
            constraint fk_cliente
                FOREIGN KEY ("ID_Cliente")
                REFERENCES "Clientes"("ID_Cliente")
                ON DELETE CASCADE
                ON UPDATE NO ACTION
                ,
            constraint fk_carro
                FOREIGN KEY ("ID_Carro")
                REFERENCES "Carros"("ID_Carro")
                ON DELETE SET NULL
                ON UPDATE NO ACTION            
        );
        '''
        self.conexao.manipularBanco(sql)
