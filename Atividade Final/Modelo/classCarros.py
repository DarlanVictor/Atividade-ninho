class Carros:
    def __init__(self, ID_Carro, Placa_Carro, Modelo_Carro, Descricao_Carro, Fabricante_Carro, Ano_Carro, Diaria_Carro):
        self._ID_Carro = ID_Carro
        self._Placa_Carro = Placa_Carro
        self._Modelo_Carro = Modelo_Carro
        self._Descricao_Carro = Descricao_Carro
        self._Fabricante_Carro = Fabricante_Carro
        self._Ano_Carro = Ano_Carro
        self._Diaria_Carro = Diaria_Carro

    def InserirCarro(self):
        placaCarro = input("Qual a placa do carro: ")
        modeloCarro = input("Qual o modelo do carro: ")
        descricaoCarro = input("Qual a descricao do carro: ")
        fabricanteCarro = input("Qual o fabricante do carro: ")
        anoCarro = input("Qual o ano de fabricação do carro: ")
        diariaCarro = input("Quanto é a diária do carro: ")
        sql = f'''
        INSERT INTO "Carros"
        VALUES(default, '{placaCarro}', '{modeloCarro}', '{descricaoCarro}', '{fabricanteCarro}', '{anoCarro}', '{diariaCarro}')
        '''
        print('Carro inserido com sucesso!')
        return sql
    

    def removerCarro(self):
        
        Idcarro = int(input("Digite o Id do carro que deseja remover?: "))
        sql = f'''
        SELECT * FROM "Carros"
        WHERE "ID_carro" = {self._ID_Carro}
        '''
        sql = f'''
        DELETE FROM "Carros"
        WHERE "ID_carro" = {Idcarro}
        '''
        print('Carro removido com sucesso!')
        return sql
