from enum import Enum

class Database:
    def __init__(self) -> None:
        self.db_type = None
        self.database_name = None
        self.connection = None
        self.cursor = None

    def execute_query(self, query, params=()):
        pass

    def close(self) -> None:
        pass

    def create_table(self, table_name, columns):
        pass

    def insert_data(self, table, data):
        pass

class DatabaseType(Enum):
    SQLITE = "sqlite"
    POSTGRES = "postgres"