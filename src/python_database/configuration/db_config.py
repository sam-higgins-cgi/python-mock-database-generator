from dotenv import dotenv_values

class Config():
	CONFIG=dotenv_values(".env")

	DATABASE_TYPE = CONFIG.get("DATABASE_TYPE", "SQLITE")

	SQLITE_PATH = CONFIG.get("SQLITE_PATH", "./src/resources/sqlite/data/example.db")
	
	POSTGRES_HOST = CONFIG.get("POSTGRES_HOST", "localhost")
	POSTGRES_PORT = CONFIG.get("POSTGRES_PORT", "5432")
	POSTGRES_USER = CONFIG.get("POSTGRES_USER", None)
	POSTGRES_DATABASE = CONFIG.get("POSTGRES_DATABASE", "postgres")

	@classmethod
	def validate(cls):
		pass