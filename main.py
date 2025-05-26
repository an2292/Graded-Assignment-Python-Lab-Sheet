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


class Client:
    """Client class for interacting with the Flight Management System Database."""

    def __init__(self, database):
        self.sql_dir = "./sql"
        self.sql_flights_dir = f"{self.sql_dir}/flights"
        self.sql_pilots_dir = f"{self.sql_dir}/pilots"
        self.sql_destinations_dir = f"{self.sql_dir}/destinations"
        self.sql_bookings_dir = f"{self.sql_dir}/bookings"
        self.sql_passengers_dir = f"{self.sql_dir}/passengers"
        self.sql_luggage_dir = f"{self.sql_dir}/luggage"
        self.db = database
        self.db.create_databases(
            f"{self.sql_dir}/create_table.sql",
            f"{self.sql_dir}/populate_table.sql",
        )

    def add_flight(self):
        print("Add a New Flight")
        self.db.run_sql(f"{self.sql_flights_dir}/add_flight.sql")

    def view_all_flights(self):
        print("View Flights by Criteria")
        self.db.run_sql(f"{self.sql_flights_dir}/view_all_flights.sql")

    def view_flights_by_departure(self, departure_id):
        print("View Flights by Departure")
        self.db.run_sql(f"{self.sql_flights_dir}/view_flights_by_departure.sql", (departure_id,))

    def view_flights_by_destination(self, destination_id):
        print("View Flights by Destination")
        self.db.run_sql(f"{self.sql_flights_dir}/view_flights_by_destination.sql", (destination_id,))

    def view_flights_by_duration(self, max_duration):
        print("View Flights by Duration")
        self.db.run_sql(f"{self.sql_flights_dir}/view_flights_by_duration.sql", (max_duration,))

    def view_flights_by_price_range(self, min_price, max_price):
        print("View Flights by Price Range")
        self.db.run_sql(f"{self.sql_flights_dir}/view_flights_by_price_range.sql", (min_price, max_price))

    def view_bookings_for_flight(self):
        print("View Bookings for Flight")
        self.db.run_sql(f"{self.sql_bookings_dir}/view_bookings_for_flight.sql")

    def view_bookings_by_date(self):
        print("View Bookings by Date")
        self.db.run_sql(f"{self.sql_bookings_dir}/view_bookings_by_date.sql") 

    def update_flight(self):
        print("Update Flight Information")
        self.db.run_sql(f"{self.sql_flights_dir}/update_flight.sql")

    def assign_pilot(self):
        print("Assign Pilot to Flight")
        self.db.run_sql(f"{self.sql_pilots_dir}/assign_pilot.sql")

    def view_pilot_schedule(self):
        print("View Pilot Schedule")
        self.db.run_sql(f"{self.sql_pilots_dir}/view_pilot_schedule.sql")

    def view_all_destinations(self):
        print("View/Update Destination Information")
        self.db.run_sql(f"{self.sql_destinations_dir}/view_all_destinations.sql")
    
    def view_destination_by_country(self):
        print("View Destination by Country")
        self.db.run_sql(f"{self.sql_destinations_dir}/view_destination_by_country.sql")

    def update_destination(self):
        print("Update Destination Information")
        self.db.run_sql(f"{self.sql_destinations_dir}/update_destination.sql")


def cli(db_name="flight"):
    """Command Line Interface for the Flight Management System."""

    db = Database(db_name)
    client = Client(db)

    def _print_menu_opts(opts):
        """Print menu options with numbers."""
        for i, opt in enumerate(opts, start=1):
            print(f"{i}. {opt}")

    while True:
        menu_opts = [
            "Add a New Flight",
            "View Flights by Criteria",
            "Update Flight Information", 
            "Assign Pilot to Flight",
            "View Pilot Schedule",
            "View/Update Destination Information",
            "View/Update Passenger Information",
            "Exit"
        ]
        _print_menu_opts(menu_opts)

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                client.add_flight()
            case "2":
                print("View Flights - Choose an option:")
                view_flights_opts = [
                    "View all flights",
                    "Filter flights",
                ]
                _print_menu_opts(view_flights_opts)
                sub_choice = input("Enter your choice: ").lower()
                if sub_choice == '1':
                    client.view_all_flights()
                elif sub_choice == '2':
                    view_flights_opts = [
                        "View Flights by Departure",
                        "View Flights by Destination",
                        "View Flights by Duration",
                        "View Flights by Price Range",
                        "Back to Main Menu",
                    ]
                    print("Choose a filter:")
                    _print_menu_opts(view_flights_opts)
                    filter_choice = input("Enter your choice: ")
                    match filter_choice:
                        case "1":
                            departure_id = input("Enter departure airport ID: ")
                            client.view_flights_by_departure(departure_id)
                        case "2":
                            destination_id = input("Enter destination airport ID: ")
                            client.view_flights_by_destination(destination_id)
                        case "3":
                            max_duration = input("Enter maximum duration: ")
                            client.view_flights_by_duration(max_duration)
                        case "4":
                            min_price = input("Enter minimum price: ")
                            max_price = input("Enter maximum price: ")
                            client.view_flights_by_price_range(min_price, max_price)
                        case "5":
                            break
                        case _:
                            print("Invalid choice. Please try again.")
            case "3":
                client.update_flight()
            case "4":
                client.assign_pilot()
            case "5":
                print("View Pilot Schedule - Choose an option:")
                view_pilot_schedule_opts = [
                    "View all pilots",
                    "View pilot by role",
                ]
                _print_menu_opts(view_pilot_schedule_opts)
                sub_choice = input("Enter your choice: ").lower()
                match sub_choice:
                    case "1":
                        client.view_pilot_schedule()
                    case "2":
                        client.view_pilot_by_role()
                    case _:
                        print("Invalid choice. Please try again.")
            case "6":
                print("View/Update Destination Information - Choose an option:")
                view_destination_opts = [
                    "View Destination",
                    "Update Destination",
                ]
                _print_menu_opts(view_destination_opts)
                sub_choice = input("Enter your choice: ").lower()
                match sub_choice:
                    case "1":
                        print("View Destination - Choose an option:")
                        view_destination_opts = [
                            "View all destinations",
                            "View destination by country",
                            "Back to Main Menu",
                        ]
                        _print_menu_opts(view_destination_opts)
                        sub_choice = input("Enter your choice: ").lower()
                        match sub_choice:
                            case "1":
                                client.view_all_destinations()
                            case "2":
                                client.view_destination_by_country()
                    case _:
                        print("Invalid choice. Please try again.")
            case "7":
                client.update_destination()
            case "8":
                print("Exiting...")
                exit()
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # TODO: Split into different .py files and run from __init__ file when done
    cli()
