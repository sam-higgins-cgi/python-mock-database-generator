class Table:
    def __init__(self, name: str, columns: list, database):
        """
        Initialise a table object.

        Parameters
        ----------
        name : str
            The name of the table.
        columns : list[Column]
            A list of column objects describing the table schema.
        database : Database
            The database connection associated with the table.
        """
        self.table_name = name
        self.columns = columns
        self.database = database

    def create_table(self):
        """
        This function is overwritten by Children of this class.
        """
        pass
    
    def insert_data(self):
        """
        This function is overwritten by Children of this class.
        """
        pass

    def get_column_names(self):
        """
        Return a list of column names in definition order.
        """
        return [column.name for column in self.columns]

    def get_column_types(self):
        """
        Return a list of column types in definition order.
        """
        return [column.type for column in self.columns]
        
    def get_column_names_and_types(self):
        """
        Return a dictionary of column names and types in definition order.
        """
        return {column.name: column.type for column in self.columns}
    
    def create_empty_row(self):
        """
        Return a dictionary representing an empty row of data for upserting.
        
        Excludes any primary key columns.
        """
        return {column.name: None for column in self.columns if not column.is_primary_key}
