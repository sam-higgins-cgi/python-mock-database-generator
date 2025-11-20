from databases.database import Database
from tables.classes.column import Column

class Table:
    def __init__(self, name: str, columns: list[Column], database: Database) -> None:
        self.table_name = name
        self.columns = columns
        self.database = database

    def get_column_names(self) -> list[str]:
        columns = []

        for c in self.columns:
            columns.append(c.name)

        return columns

    def get_column_types(self) -> list[str]:
        types = []

        for c in self.columns:
            types.append(c.type)

        return types

    def get_column_names_and_types(self) -> dict[str, str]:
        return dict(zip(self.get_column_names(), self.get_column_types()))
    
    def create_empty_row(self) -> dict[str, str]:
        object: dict[str, str] = {}
        
        for c in self.columns:
            if not c.is_primary_key:
                object[c.name] = ""

        return object

    def create_table(self) -> None:
        pass
    
    def insert_data(self) -> None:
        pass


