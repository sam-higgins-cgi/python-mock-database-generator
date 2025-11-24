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
    pass

if (os.path.exists(Config.SQLITE_PATH)): os.remove(Config.SQLITE_PATH)

match (Config.DATABASE_TYPE.lower()):
    case SupportedDatabases.SQLITE: database = DatabaseSqlite()
    case SupportedDatabases.POSTGRES: database = DatabasePostgres()
    case _: print(f"Invalid Database Type: {Config.DATABASE_TYPE}")

if Config.DATABASE_TYPE == SupportedDatabases.POSTGRES: database.execute_query("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")

start_time = dt.now()

user_table = Users(database)
book_table = Books(database)
userbooks_table = UserBooks(database)

user_table.create_table()
book_table.create_table()
userbooks_table.create_table()

user_table.insert_fake_data(1000)
book_table.insert_fake_data(1000)
userbooks_table.insert_fake_data(1000)

end_time = dt.now()

users = database.execute_query(f"SELECT * FROM {user_table.table_name} ORDER BY RANDOM() LIMIT 2;")
books = database.execute_query(f"SELECT * FROM {book_table.table_name} ORDER BY RANDOM() LIMIT 2;")
userbooks = database.execute_query(f"SELECT * FROM {userbooks_table.table_name} ORDER BY RANDOM() LIMIT 2;")

print("**USERS**")
for row in users: print(json.dumps(dict(zip(user_table.get_column_names(), [str(value) for value in row])), indent=2))

print("**BOOKS**")
for row in books: print(json.dumps(dict(zip(book_table.get_column_names(), [str(value) for value in row])), indent=2))

print("**USER_BOOKS**")
for row in userbooks: print(json.dumps(dict(zip(userbooks_table.get_column_names(), [str(value) for value in row])), indent=2))

# database.execute_query("""
#     SELECT
#         ub.user_id,
#         --u.first_name,
#         --u.last_name,
#         u.country,
#         ub.book_id,
#         b.title,
#         b.author,
#         b.genre,
#         ub.book_returned
#     FROM user_books AS ub
#     LEFT JOIN users AS u
#         ON ub.user_id = u.id
#     LEFT JOIN books AS b
#         ON ub.book_id = b.id
#     ORDER BY ub.user_id ASC
# """)

print(f"""
start: {start_time.strftime("%H:%M:%S.%f")}
end  : {end_time.strftime("%H:%M:%S.%f")}
run  : {abs(end_time - start_time).total_seconds()}
""")

database.close()