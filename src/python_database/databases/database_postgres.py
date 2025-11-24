from configuration.db_config import Config
from databases.database import Database
from databases.supported_databases import SupportedDatabases

import psycopg2

class DatabasePostgres(Database):
    def __init__(self):
        self.db_type = SupportedDatabases.POSTGRES
        self.database_name = Config.POSTGRES_DATABASE
        self.connection = psycopg2.connect(
            host=Config.POSTGRES_HOST, 
            dbname=Config.POSTGRES_DATABASE, 
            user=Config.POSTGRES_USER, 
            port=Config.POSTGRES_PORT
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        if self.cursor.description == None: 
            return [] 
        else: 
            return self.cursor.fetchall()

    def close(self) -> None:
        self.connection.close()

    def create_table(self, table_name: str, columns: list):
        column_definitions = []

        for column in columns:
            definition = " ".join(filter(None, [
                column.name, 
                column.type, 
                "NULL" if column.is_nullable else "NOT NULL",
                f"DEFAULT {column.default}" if column.default is not None else "",
                "UNIQUE" if column.is_unique else ""                
            ]))
            column_definitions.append(definition)

        primary_key_columns = [column.name for column in columns if column.is_primary_key]

        if primary_key_columns:
            primary_key = f"PRIMARY KEY ({", ".join(primary_key_columns)})"
            column_definitions.append(primary_key)

        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({", ".join(column_definitions)})"
        
        #print(query)

        self.execute_query(query)

    def insert_data(self, table, data: list[dict]):

        column_type_lookup = table.get_column_names_and_types()

        insert_column_names = ", ".join(data[0].keys())

        value_list = []

        for row in data:
            row_values = []
            for column_name, column_value in row.items():
                if (column_value is None):
                    row_values.append("NULL")
                else:
                    match (column_type_lookup[column_name]):
                        case "INTEGER" | "INT": row_values.append(f"{column_value}")
                        case "DATE": row_values.append(f"\'{column_value.strftime("%d/%m/%Y")}\'")
                        case "DATETIME" | "TIMESTAMP": row_values.append(f"\'{column_value.strftime("%d/%m/%Y %H:%M:%S.%f")}\'")
                        case _: row_values.append(f"\'{column_value.replace("'", "''")}\'")
            value_list.append(f"({", ".join(row_values)})")
        
        insert_values = ", ".join(value_list)

        query = f"INSERT INTO {table.table_name} ({insert_column_names}) VALUES {insert_values}"
       
        #print(query)
        
        self.execute_query(query)
