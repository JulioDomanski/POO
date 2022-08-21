class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def like(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):
        return f'Nome: {self.nome} - Likes: {self.like}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Duracao: {self.duracao} minutos - likes: {self.like}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporada = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - Temporadas: {self.temporada} - Likes: {self.like}'

class playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    def __len__(self):
        return len(self._programa)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

listinha = [vingadores, atlanta, tmep, demolidor]
minha_playlist = playlist('final de semana', listinha)
for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist)}')



