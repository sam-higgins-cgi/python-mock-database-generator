from databases.database import DatabaseType
from databases.database_sqlite import DatabaseSqlite
from databases.database_postgres import DatabasePostgres
from tables.objects.users import Users
from tables.objects.books import Books
from datetime import datetime as dt

import os

db = DatabaseType.SQLITE

if (os.path.exists("./src/resources/sqlite/data/example.db")): os.remove("./src/resources/sqlite/data/example.db")

match (db):
    case DatabaseType.SQLITE: database = DatabaseSqlite('./src/resources/sqlite/data/example.db')
    case DatabaseType.POSTGRES: database = DatabasePostgres('postgres_db')
    case _: print(f"Invalid Database Type: {db}")

if db == DatabaseType.POSTGRES: database.execute_query("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")

start_time = dt.now()
end_time = None

user_table = Users(database)
book_table = Books(database)

user_table.create_table()
book_table.create_table()

user_table.insert_fake_data(1000)
book_table.insert_fake_data(1000)

end_time = dt.now()

users = database.execute_query(f"SELECT * FROM { "" if db == DatabaseType.SQLITE else "public." }users ORDER BY RANDOM() LIMIT 5;")
books = database.execute_query(f"SELECT * FROM { "" if db == DatabaseType.SQLITE else "public." }books ORDER BY RANDOM() LIMIT 5;")

for row in users:
    print(f"User = {row}")

print()

for row in books:
    print(f"Book = {row}")


print(f"""
start: {start_time.strftime("%H:%M:%S.%f")}
end  : {end_time.strftime("%H:%M:%S.%f")}
run  : {abs(end_time - start_time).total_seconds()}
""")

database.close()