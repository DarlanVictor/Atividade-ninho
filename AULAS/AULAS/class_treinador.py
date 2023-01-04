import random

listaNomes = ('Jose', 'Maria', 'Marcos', 'Charles')

class Treinador:
    def __init__(self,nome='',pokemons=[]):
        self.pokemons = pokemons
        if nome == '':
            self._nome = random.choice(listaNomes)
