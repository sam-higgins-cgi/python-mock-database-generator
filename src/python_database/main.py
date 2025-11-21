import json
from databases.database import DatabaseType
from databases.database_sqlite import DatabaseSqlite
from databases.database_postgres import DatabasePostgres
from tables.objects.users import Users
from tables.objects.books import Books
from datetime import datetime as dt

import os

db = DatabaseType.POSTGRES

if (os.path.exists("./src/resources/sqlite/data/example.db")): os.remove("./src/resources/sqlite/data/example.db")

match (db):
    case DatabaseType.SQLITE: database = DatabaseSqlite('./src/resources/sqlite/data/example.db')
    case DatabaseType.POSTGRES: database = DatabasePostgres(DatabaseType.POSTGRES.value)
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

users = database.execute_query(f"SELECT * FROM {user_table.table_name} ORDER BY RANDOM() LIMIT 2;")
books = database.execute_query(f"SELECT * FROM {book_table.table_name} ORDER BY RANDOM() LIMIT 2;")

print("**USERS**")
for row in users: print(json.dumps(dict(zip(user_table.get_column_names(), [str(value) for value in row])), indent=2))

# print("**BOOKS**")
# for row in books: print(json.dumps(dict(zip(book_table.get_column_names(), [str(value) for value in row])), indent=2))


print(f"""
start: {start_time.strftime("%H:%M:%S.%f")}
end  : {end_time.strftime("%H:%M:%S.%f")}
run  : {abs(end_time - start_time).total_seconds()}
""")

database.close()