class Pokemon:
    def __init__(self,nome,ataque,defesa,agilidade,hp):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade
        self.hp = hp
    def checar_Vantagem(self,pokemonInimigo):
        if(pokemonInimigo.tipo == 'Fogo'):
            print('Vantagem contra: Inseto, Planta, Gelo')
            print('Desvantagem contra: Pedra, Água')
        elif(pokemonInimigo.tipo == 'Água'):
            print('Vantagens: Fogo, Terrestre e Pedra')
            print('Desvantagens: Elétrico e Planta')
        elif(pokemonInimigo.tipo == 'Eletrico'):
            print('Vantagens: Água e Voador')
            print('Desvantagens: Pedra')
        elif(pokemonInimigo.tipo == 'Planta'):
            print('Vantagens: Terrestre, Pedra e Água')
            print('Desvantagens: Inseto, Fogo, Voador, Gelo')
        elif(pokemonInimigo.tipo == 'Dragão'):
            print('Vantagens: Dragão')
            print('Desvantagens: Dragão, Fada e Gelo')
        elif(pokemonInimigo.tipo == 'Psiquico'):
            print('')
            print('')
        elif(pokemonInimigo.tipo == 'Fantasma'):
            print('')
            print('')
        elif(pokemonInimigo.tipo == 'Voador'):
            print('')
            print('')
        elif(pokemonInimigo.tipo == 'Gelo'):
            print('')
            print('')
        elif(pokemonInimigo.tipo == 'Inseto'):
            print('')
            print('')
        elif(pokemonInimigo.tipo == 'Lutador'):
            print('')
            print('')
        elif(pokemonInimigo.tipo == 'Pedra'):
            print('')
            print('')
        elif(pokemonInimigo.tipo == 'Normal'):
            print('')
            print('')    

class Pokemon_Fogo(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Fogo'
class Pokemon_Aquatico(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Água'
class Pokemon_Eletrico(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Eletrico'
class Pokemon_Planta(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Planta'
class Pokemon_Dragão(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Dragão'
class Pokemon_Psiquico(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Psiquico'
class Pokemon_Fantasma(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Fantasma'
class Pokemon_Voador(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Voador'
class Pokemon_Gelo(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Gelo'
class Pokemon_Inseto(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Inseto'
class Pokemon_Lutador(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Lutador'
class Pokemon_Pedra(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Pedra'
class Pokemon_Normal(Pokemon):
    def __init__(self, nome, ataque, defesa, agilidade, hp):
        super().__init__(nome, ataque, defesa, agilidade, hp)
        self.tipo = 'Normal'
