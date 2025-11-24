from data.data_generator import DataGenerator
from databases.supported_databases import SupportedDatabases
from datetime import datetime
from random import choice, random
from tables.classes.column import Column
from tables.classes.table import Table

class UserBooks(Table):
    columns_sqlite = [
            Column("id", "INTEGER", is_nullable=False, is_primary_key=True),
            Column("user_id", "INT"),
            Column("book_id", "INT"),
            Column("book_returned", "INT"),
            Column("date_added", "DATETIME")
    ]

    columns_postgres = [
            Column("id", "SERIAL", is_nullable=False, is_primary_key=True),
            Column("user_id", "INT"),
            Column("book_id", "INT"),
            Column("book_returned", "INT"),
            Column("date_added", "TIMESTAMP")
    ]

    def __init__(self, database):
        self.table_name = "user_books"
        self.database = database
        self.faker = DataGenerator()
        match (database.db_type):
            case SupportedDatabases.SQLITE: self.columns = self.columns_sqlite
            case SupportedDatabases.POSTGRES: self.columns = self.columns_postgres

    def generate_fake_data(self, rows):
        data = []
        
        user_ids = [id[0] for id in self.database.execute_query("SELECT id FROM users ORDER BY RANDOM()")]
        book_ids = [id[0] for id in self.database.execute_query("SELECT id FROM books ORDER BY RANDOM()")]

        for _ in range(rows):
            row = super().create_empty_row()

            row["user_id"] = choice(user_ids)
            row["book_id"] = choice(book_ids)
            row["book_returned"] = 1 if random() > 0.5 else 0
            row["date_added"] = datetime.now()

            data.append(row)

        return data
    
    def create_table(self):
        self.database.create_table(self.table_name, self.columns)

    def insert_fake_data(self, rows):
        self.database.insert_data(self, self.generate_fake_data(rows))