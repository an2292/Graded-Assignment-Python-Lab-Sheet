import sqlite3
from pathlib import Path
from contextlib import contextmanager

class Database:
    """Database manager class for handling SQLite database operations."""

    def __init__(self, db_name="app"):
        self.db_name = db_name
        self.db_path = f"{db_name}.db"

    @contextmanager
    def get_db_connection(self):
        """
        Helper class for managing database connections and ensuring they are closed properly.

        Details of handling external resource usage effectively to ensure resources are relased are
        detaled in the below article which also demonstrates the use of context managers:
        https://realpython.com/python-with-statement/
        """

        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def run_sql(self, filepath, params=None):
        """
        Run SQL statements from a file, the function is used to run both SELECT and INSERT statements.
        For SELECT statements, the function will print the results to the console.
        For INSERT statements, the function will commit the changes to the database.
        """

        sql_file = Path(filepath)
        if not sql_file.exists():
            raise FileNotFoundError(f"SQL file {filepath} does not exist.")

        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            sql_script = sql_file.read_text(encoding="utf-8").strip()

            if sql_script.upper().startswith("SELECT"):
                # Params can't be none, so set to empty tuple if no params are needed
                current_params = params if params is not None else ()
                cursor.execute(sql_script, current_params)
                rows = cursor.fetchall()
                if rows:
                    column_names = [description[0] for description in cursor.description]
                    print("\n--- Query Results ---")
                    print(column_names)
                    for row in rows:
                        print(row)
                    print("---------------------\n")
                else:
                    print("\n--- Query Results ---")
                    print("No data found for your query.")
                    print("---------------------\n")
            else:
                cursor.executescript(sql_script)
                conn.commit()

    def create_databases(self, create_table_script, populate_table_script):
        """Create databases for the application and seed them with test data."""

        try:
            # Create tables
            self.run_sql(create_table_script)
            print("Tables created.")

            self.run_sql(populate_table_script)
            print("Tables populated with test data.")

        except Exception as e:
            print(f"An error occurred: {e}")
            raise