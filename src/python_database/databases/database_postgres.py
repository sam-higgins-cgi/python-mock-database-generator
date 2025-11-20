from databases.database import Database, DatabaseType
from tables.classes.table import Table
import psycopg2


class DatabasePostgres(Database):
    def __init__(self, db_name):
        self.db_type = DatabaseType.POSTGRES
        self.database_name = db_name
        self.connection = psycopg2.connect(host="localhost", dbname=db_name, user="sam.higgins", port="5432")
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        if self.cursor.description == None: 
            return [] 
        else: 
            return self.cursor.fetchall()

    def close(self):
        self.connection.close()

    def create_table(self, table_name, columns) -> None:
        query = f"CREATE TABLE IF NOT EXISTS public.{table_name} ()"
        
        column_definitions = []

        for definition in columns:
            tokens = [definition.name, definition.type]

            if definition.is_primary_key: tokens.append("PRIMARY KEY") 

            tokens.append(definition.nullable)

            column_definitions.append(" ".join(tokens))

        query = query.replace("()", f"({", ".join(column_definitions)})")

        #print(query)

        self.execute_query(query)

    def insert_data(self, table: Table, data: list[dict]):
        query = f"INSERT INTO {table.table_name} (columns) VALUES (values)"

        column_types = table.get_column_names_and_types()

        insert_columns = ", ".join(data[0].keys())

        query = query.replace("(columns)", f"({insert_columns})")

        value_list = []

        for r in data:
            row_values = []
            for k, v in r.items():
                type = column_types[k]

                match (type):
                    case "INTEGER" | "INT": row_values.append(f"{v}")
                    case "DATE": row_values.append(f"\'{v.strftime("%d/%m/%Y")}\'")
                    case "DATETIME" | "TIMESTAMP": row_values.append(f"\'{v.strftime("%d/%m/%Y %H:%M:%S.%f")}\'")
                    case _: row_values.append(f"\'{v.replace("'", "''")}\'")
            
            value_list.append(f"({", ".join(row_values)})")
        
        values = ", ".join(value_list)

        query = query.replace("(values)", f"{values}")
        
        #print(query)

        self.execute_query(query)
