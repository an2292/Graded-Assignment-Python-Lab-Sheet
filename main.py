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
    """Client class for interacting with the Flight Management System Database."""

    def __init__(self, database):
        self.db = database
        self.db.create_databases()

    # Add a New Flight
    def add_flight(self):
        print("Add a New Flight")

    # View Flights by Criteria
    def view_flights(self):
        print("View Flights by Criteria")

    # Update Flight Information
    def update_flight(self):
        print("Update Flight Information")

    # Assign Pilot to Flight
    def assign_pilot(self):
        print("Assign Pilot to Flight")

    # View Pilot Schedule
    def view_pilot_schedule(self):
        print("View Pilot Schedule")

    # View/Update Destination Information
    def view_update_destination(self):
        print("View/Update Destination Information")


def cli(db_name="flight"):
    """Command Line Interface for the Flight Management System."""

    db = Database(db_name)
    client = Client(db)

    while True:
        print("1. Add a New Flight")
        print("2. View Flights by Criteria")
        print("3. Update Flight Information")
        print("4. Assign Pilot to Flight")
        print("5. View Pilot Schedule")
        print("6. View/Update Destination Information")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                client.add_flight()
            case "2":
                client.view_flights()
            case "3":
                client.update_flight()
            case "4":
                client.assign_pilot()
            case "5":
                client.view_pilot_schedule()
            case "6":
                client.view_update_destination()
            case "7":
                print("Exiting...")
                exit()
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cli()
