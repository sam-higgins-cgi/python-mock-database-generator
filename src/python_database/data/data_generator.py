from faker import Faker
from random import choice

from data.providers.genre_provider import GenreProvider

class DataGenerator:
    def __init__(self) -> None:
        self.fakeUK = Faker('en_GB')
        self.fakeDE = Faker('de_DE')
        self.fakeFR = Faker('fr_FR')
        self.fakeCAEN = Faker('en_CA')
        self.fakeCAFR = Faker('fr_CA')

        self.all_fakes = [self.fakeUK, self.fakeDE, self.fakeFR, self.fakeCAEN, self.fakeCAFR]

    def get_random_faker(self):
        faker = choice(self.all_fakes)

        faker.add_provider(GenreProvider)
        
        return faker
    