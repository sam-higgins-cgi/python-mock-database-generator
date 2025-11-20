from faker.providers import BaseProvider

class GenreProvider(BaseProvider):
    genres = [
        "Fantasy",
        "Science Fiction",
        "Mystery",
        "Thriller",
        "Romance",
        "Horror",
        "Historical",
        "Drama",
        "Comedy",
        "Adventure",
        "Cyberpunk",
        "Space Opera",
        "Mythpunk",
        "Noir",
        "Magical Realism"
    ]

    def genre(self):
        return self.random_element(self.genres)