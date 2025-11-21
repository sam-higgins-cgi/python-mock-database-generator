from databases.database import DatabaseType
from tables.classes.column import Column
from tables.classes.table import Table
from data.data_generator import DataGenerator
from datetime import datetime

class Books(Table):
    columns_sqlite = [
            Column("id", "INTEGER", is_nullable=False, is_primary_key=True),
            Column("title", "TEXT"),
            Column("author", "TEXT"),
            Column("date_published", "DATE"),
            Column("genre", "TEXT"),
            Column("language", "TEXT"),
            Column("isbn", "TEXT"),
            Column("date_added", "DATETIME")
    ]

    columns_postgres = [
            Column("id", "SERIAL", is_nullable=False, is_primary_key=True),
            Column("title", "VARCHAR"),
            Column("author", "VARCHAR"),
            Column("date_published", "DATE"),
            Column("genre", "VARCHAR"),
            Column("language", "VARCHAR"),
            Column("isbn", "VARCHAR"),
            Column("date_added", "TIMESTAMP")
    ]

    def __init__(self, database):
        self.table_name = "books"
        self.database = database
        self.faker = DataGenerator()
        match (database.db_type):
            case DatabaseType.SQLITE: self.columns = self.columns_sqlite
            case DatabaseType.POSTGRES: self.columns = self.columns_postgres

    def generate_fake_data(self, rows):
        data = []

        for _ in range(rows):
            row = super().create_empty_row()
            faker = self.faker.get_random_faker()

            row["title"] = " ".join(faker.words(2))
            row["author"] = faker.name()
            row["date_published"] = faker.date_of_birth()
            row["genre"] = faker.genre()
            row["language"] = faker.language_name()
            row["isbn"] = faker.isbn10()
            row["date_added"] = datetime.now()

            data.append(row)

        return data
    
    def create_table(self):
        self.database.create_table(self.table_name, self.columns)

    def insert_fake_data(self, rows):
        self.database.insert_data(self, self.generate_fake_data(rows))