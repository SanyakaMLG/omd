class BasePokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    def __str__(self):
        emoji_dict = {
            'electric': '⚡️',
            'grass': '🌿',
            'water': '💧',
        }
        return f'{self.name}/{emoji_dict[self.poketype]}'


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    pikachu = Pokemon('Pikachu', 'electric')
    print(pikachu)
