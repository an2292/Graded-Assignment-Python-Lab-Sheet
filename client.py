from database import Database


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

    def view_flights_by_date(self, date):
        print("View Flights by Date")
        self.db.run_sql(f"{self.sql_bookings_dir}/view_flights_by_departure_date.sql", (date,))

    def count_passengers_on_flight(self, flight_id):
        print("Count Passengers on Flight")
        self.db.run_sql(f"{self.sql_flights_dir}/count_passengers_on_flight.sql", (flight_id,))

    def count_pilots_assigned_to_flight(self, flight_id):
        print("Count Pilots Assigned to Flight")
        self.db.run_sql(f"{self.sql_flights_dir}/count_pilots_assigned_to_flight.sql", (flight_id,))

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
