class Column:
    def __init__(
            self, 
            name: str, 
            type: str, 
            is_nullable: bool = False, 
            is_primary_key: bool = False,
            is_unique: bool = False,
            is_incrementing: bool = False,
            default = None
    ):
        """
        Represent a single column in a table schema.

        Parameters
        ----------
        name : str
            The column name.
        type : str
            The SQL data type for the column (e.g., "TEXT", "INTEGER").
        is_nullable : bool, optional
            Whether the column allows NULL values. Defaults to False.
        is_primary_key : bool, optional
            Whether the column is part of the table's primary key. Defaults to False.
        is_unique : bool, optional
            Whether the column has a UNIQUE constraint. Defaults to False.
        is_incrementing : bool, optional
            Whether the column auto-increments (for numeric PKs). Defaults to False.
        deafult : any, optional
            A default value for the column, will implement a DEFAULT constraint. Defaults to None.
        """
        self.name = name
        self.type = type
        self.is_nullable = is_nullable
        self.is_primary_key = is_primary_key
        self.is_unique = is_unique
        self.is_incrementing = is_incrementing
        self.default = default