class Pokemon:
    def __init__(self, nome, tipo, ataque, hp):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.hp = hp

pokemon1 = Pokemon("Bulbasauro", "planta", 30, 100)
print(f"""Meu pokemon:
Nome: {pokemon1.nome}
Tipo: {pokemon1.tipo}
Ataque: {pokemon1.ataque}
Hp: {pokemon1.hp}
\n""")

