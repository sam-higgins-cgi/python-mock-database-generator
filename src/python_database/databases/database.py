class Database:
    def __init__(self):
        self.db_type = None
        self.database_name = None
        self.connection = None
        self.cursor = None

    def execute_query(self, query: str, params=()):
        pass

    def close(self):
        pass

    def create_table(self, table_name: str, columns: list):
        pass

    def insert_data(self, table, data: list[dict]):
        pass
