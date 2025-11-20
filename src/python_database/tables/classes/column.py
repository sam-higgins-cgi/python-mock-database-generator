class Column:
    def __init__(
            self, 
            name: str, 
            type: str, 
            is_nullable: bool = False, 
            is_primary_key: bool = False,
            is_unique: bool = False,
            is_incrementing: bool = False
    ):
        self.name = name
        self.type = type
        self.nullable = "NULL" if is_nullable else "NOT NULL"
        self.is_primary_key = is_primary_key
        self.is_unique = is_unique
        self.is_incrementing = is_incrementing