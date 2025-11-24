# Description
A Python tool to generate mock databases and populate them with realistic data.

# Technologies
- Python 3.14
- Poetry
- Faker
- Psycopg2
- Python-dotenv
- SQLite
- PostgreSQL

# Runbook
1. Use the `.env.example` to create a `.env` file with the required config.
	-  If using SQLite then you can provide a file location for the `.db` file.
	- If using Postgres, ensure the server is running and provide the connection details.

2. `poetry install`

3. `poetry run python .\src\python_database\main.py` 