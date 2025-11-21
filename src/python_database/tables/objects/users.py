import random
from databases.database import DatabaseType
from tables.classes.column import Column
from tables.classes.table import Table
from data.data_generator import DataGenerator
from datetime import datetime

class Users(Table):
    columns_sqlite = [
        Column("id", "INTEGER", is_nullable=False, is_primary_key=True),
        Column("first_name", "TEXT"),
        Column("last_name", "TEXT"),
        Column("date_of_birth", "DATE"),
        Column("address", "TEXT"),
        Column("city", "TEXT"),
        Column("post_code", "TEXT"),
        Column("country", "TEXT"),
        Column("phone_number", "TEXT", is_nullable=True),
        Column("email", "TEXT", is_nullable=True),
        Column("role", "INT"),
        Column("date_added", "DATETIME"),
        Column("is_deleted", "INT"),
    ]

    columns_postgres = [
        Column("id", "SERIAL", is_nullable=False, is_primary_key=True),
        Column("first_name", "VARCHAR"),
        Column("last_name", "VARCHAR"),
        Column("date_of_birth", "DATE"),
        Column("address", "VARCHAR"),
        Column("city", "VARCHAR"),
        Column("post_code", "VARCHAR"),
        Column("country", "VARCHAR"),
        Column("phone_number", "VARCHAR", is_nullable=True),
        Column("email", "VARCHAR", is_nullable=True),
        Column("role", "INT"),
        Column("date_added", "TIMESTAMP"),
        Column("is_deleted", "INT"),
    ]

    def __init__(self, database):
        self.table_name = "users"
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

            row["first_name"] = faker.first_name()
            row["last_name"] = faker.last_name()
            row["date_of_birth"] = faker.date_of_birth()
            row["address"] = faker.street_address()
            row["city"] = faker.city()
            row["post_code"] = faker.postcode()
            row["country"] = faker.current_country_code()
            row["phone_number"] = faker.phone_number() if random.random() > 0.2 else None
            row["email"] = faker.email() if random.random() > 0.2 else None
            row["role"] = 1
            row["date_added"] = datetime.now()
            row["is_deleted"] = 0

            data.append(row)

        return data
    
    def create_table(self):
        self.database.create_table(self.table_name, self.columns)

    def insert_fake_data(self, rows):
        self.database.insert_data(self, self.generate_fake_data(rows))

