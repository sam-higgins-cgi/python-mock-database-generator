import json
import os

from configuration.db_config import Config
from databases.database_postgres import DatabasePostgres
from databases.database_sqlite import DatabaseSqlite
from databases.supported_databases import SupportedDatabases
from datetime import datetime as dt
from tables.objects.userbooks import UserBooks
from tables.objects.users import Users
from tables.objects.books import Books

def main():
    match (Config.DATABASE_TYPE.lower()):
        case SupportedDatabases.SQLITE: database = DatabaseSqlite()
        case SupportedDatabases.POSTGRES: database = DatabasePostgres()
        case _: print(f"Invalid Database Type: {Config.DATABASE_TYPE}")

    start_time = dt.now()

    tables = [
        Users(database), 
        Books(database), 
        UserBooks(database)
    ]

    for table in tables:
        database.drop_table(table.table_name)
        table.create_table()
        table.insert_fake_data(1000)

    end_time = dt.now()

    print(f"""
        start: {start_time.strftime("%H:%M:%S.%f")}
        end  : {end_time.strftime("%H:%M:%S.%f")}
        run  : {abs(end_time - start_time).total_seconds()}
    """)

    database.close()

if __name__ == "__main__":
    main()
