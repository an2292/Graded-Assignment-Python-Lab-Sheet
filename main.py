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

    def run_sql(self, filepath):
        """Run SQL statements from a file."""

        sql_file = Path(filepath)
        if not sql_file.exists():
            raise FileNotFoundError(f"SQL file {filepath} does not exist.")

        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            sql_script = sql_file.read_text(encoding="utf-8")
            cursor.executescript(sql_script)
            conn.commit()

    def create_databases(
        self,
        create_table_script="./create-table.sql",
        populate_table_script="./populate-table.sql",
    ):
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


class Client:
    def __init__(self):
        self.name = ""


def cli():
    flight_db = Database("flight")
    flight_db.create_databases()


if __name__ == "__main__":
    cli()
