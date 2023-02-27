'''Atividade para casa:
Crie uma banco de dados de uma Biblioteca que deverá conter a seguinte tabela:
Livros:
Livro_id
Livro_nome
Livro_paginas
Livro_anoLançamento
Livro_autor
- Especificar os tipos de cada atributo e criar função no python createTableLivros
- Usar o código abaixo para criar um CRUD, sistema de gerenciamento da tabela
CRUD significa Create, Read, Update, Delete e se refere as operações básicas que podemos realizar
com os campos de um tabela de um banco de dados.
Create - Inserir um novo campo. Exemplo: Inserir um novo funcionário na tabela Funcionários
Read - Relacionado ao comando Select, é o ato de ler e imprimir todos os campos ou campos específicos de uma tabela
Update - Atualizar um campo da tabela
Delete - Remover uma entrada da tabela. Ex: Remover um funcionário
'''

import psycopg2

def criarTabelaLivros(cur, conexao):
    cur.execute('''
    DROP TABLE IF EXISTS "Livros";

    CREATE TABLE "Livros"(
        "Livro_id" int GENERATED ALWAYS AS IDENTITY,
        "Livro_nome" varchar(255),
        "Livro_paginas" int,
        "Livro_anoLançamento" char(4),
        "Livro_autorID" int,
        CONSTRAINT fk_Autor
            FOREIGN KEY("Livro_autorID")
            REFERENCES "Autores"("Autor_id")
            ON DELETE NO ACTION
            ON UPDATE NO ACTION
            ,

        PRIMARY KEY("Livro_id")
    );
    ''')
    conexao.commit()
    print("Tabela criada com sucesso!")

def criarTabelaAutor(cur, conexao):
    cur.execute('''
    DROP TABLE IF EXISTS "Autores";

    CREATE TABLE "Autores"(
        "Autor_id" int GENERATED ALWAYS AS IDENTITY,
        "Autor_nome" varchar(255),
        PRIMARY KEY("Autor_id")
    );
    ''')
    conexao.commit()
    print("Tabela criada com sucesso!")


def inserirLivros(cur, conexao):
    print("Adicinando livros...")
    livroNome = input('Qual o nome do livro?: ')
    livroPaginas = input('Quantas paginas tem o livro?: ')
    livroAnoLan = input('Qual o ano de lançamento do livro?: ')
    verAutor(cur, conexao)
    livroAutorID = input('Qual o id do autor do livro?: ')
    cur.execute(f'''
    INSERT INTO "Livros"
    VALUES(DEFAULT, '{livroNome}', '{livroPaginas}', '{livroAnoLan}', '{livroAutorID}')
    ''')
    conexao.commit()
    print("Adicionado com sucesso!")

def adicionarAutor(cur, conexao):
    addAutor = input('Qual o nome do autor que deseja adicionar?: ')
    cur.execute(f'''
    INSERT INTO "Autores"
    VALUES(DEFAULT, '{addAutor}')
    ''')
    conexao.commit()
    print("Autor adicionado com sucesso!")

def verAutor(cur, conexao):
    cur.execute(f'''
    SELECT * FROM "Autores"
    ''')
    conexao.commit()
    autores = cursor.fetchall()
    for autor in autores:
        print(f"{autor[0]} | {autor[1]}")

def verLivros(cur, conexao):
    cur.execute('''
    SELECT * FROM "Livros"
    ''')
    conexao.commit()
    livros = cursor.fetchall()
    for livro in livros:
        
        print(f'{livro[0]} | {livro[1]} | {livro[2]} | {livro[3]} | {livro[4]}')
    

def atualizarLivros(cur, conexao):
    verLivros(cur, conexao)
    livroID = int(input('Qual o id do livro que deseja atualizar?: '))
    cur.execute(f'''
    SELECT * FROM "Livros"
    WHERE "Livro_id" = {livroID}
    ''')
    print("Atualizando os dados do livro...", cursor.fetchone())
    novoNome = input("Qual o nome do livro?: ")
    quantPaginas = input("Quantas paginas tem o livro?: ")
    anoLan = input("Qual o ano de lançamento do livro?: ")
    livroIdAutor = input("Qual o id do autor do livro?: ")
    cur.execute(f'''
    UPDATE "Livros"
    SET "Livro_nome" = '{novoNome}', "Livro_paginas" = '{quantPaginas}', "Livro_anoLançamento" = '{anoLan}', "Livro_autorID" = '{livroIdAutor}'
    WHERE "Livro_id" = '{livroID}'
    ''')
    conexao.commit()
    print("Atualizado com sucesso!")

def removerLivros(cur, conexao):
    verLivros(cur, conexao)
    livroID = int(input("Qual id do livro para remover?: "))
    cur.execute(f'''
    DELETE FROM "Livros"
    WHERE "Livro_id" = '{livroID}'
    ''')
    conexao.commit()
    print("Removido com sucesso!")

def removerAutor(cur, conexao):
    verAutor(cur, conexao)
    autorID = int(input("Qual o id do autor para remover?: "))
    cur.execute(f'''
    DELETE FROM "Autores"
    WHERE "Autor_id" = '{autorID}'
    ''')
    conexao.commit()
    print('Autor removido com sucesso!')

while True:    
    try:
        con = psycopg2.connect(database="Biblioteca", user="postgres", password="postgres", host="localhost", port="5432")

        cursor = con.cursor()
        print("Conectado")

        print(''' 
    Bem vindo a Biblioteca

    [1] Ver Livros
    [2] Adicionar livros
    [3] Remover livros
    [4] Atualizar livro
    [5] Ver Autores
    [6] Adicionar Autor
    [7] Remover Autor
    [8] Sair
        ''')

        opçoesMenu = input('Digite a opção desejada: ')

        match opçoesMenu:
            case "1":
                verLivros(cursor, con)
            case "2":
                inserirLivros(cursor, con)
            case "3":
                removerLivros(cursor, con)
            case "4":
                atualizarLivros(cursor, con)
            case "5":
                verAutor(cursor, con)
            case "6":
                adicionarAutor(cursor, con)
            case "7":
                removerAutor(cursor, con)
            case "8":
                print('Finalizando...Até mais')
                break
            case _:
                print('Opção Inválida')

        input('Tecle enter para continuar')

        cursor.close()
        con.close()

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)
