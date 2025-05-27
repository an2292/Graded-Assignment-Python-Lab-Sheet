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

    # ========================================
    # FLIGHT MANAGEMENT METHODS
    # ========================================

    def add_flight(self, departure_airport_id, destination_airport_id, duration, price, status, departure_datetime):
        print("Add a New Flight")
        self.db.run_sql(f"{self.sql_flights_dir}/add_flight.sql", (departure_airport_id, destination_airport_id, duration, price, status, departure_datetime))

    def view_all_flights(self):
        print("View All Flights")
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

    def view_flights_by_date(self, departure_date):
        print("View Flights by Departure Date")
        self.db.run_sql(f"{self.sql_flights_dir}/view_flights_by_departure_date.sql", (departure_date,))

    def view_flights_by_status(self, status):
        print("View Flights by Status")
        self.db.run_sql(f"{self.sql_flights_dir}/view_flights_by_status.sql", (status,))

    def update_flight(self, flight_id, departure_airport_id, destination_airport_id, duration, price):
        print("Update Flight Information")
        self.db.run_sql(f"{self.sql_flights_dir}/update_flight.sql", (departure_airport_id, destination_airport_id, duration, price, flight_id))

    def update_flight_status(self, flight_id, new_status):
        print("Update Flight Status")
        self.db.run_sql(f"{self.sql_flights_dir}/update_flight_status.sql", (new_status, flight_id))

    def update_flight_departure_time(self, flight_id, new_departure_datetime):
        print("Update Flight Departure Time")
        self.db.run_sql(f"{self.sql_flights_dir}/update_flight_departure_time.sql", (new_departure_datetime, flight_id))

    def summary_flights_per_destination(self):
        print("Summary of Flights per Destination")
        self.db.run_sql(f"{self.sql_flights_dir}/summary_flights_per_destination.sql")

    def count_pilots_assigned_to_flight(self, flight_id):
        print("Count Pilots Assigned to Flight")
        self.db.run_sql(f"{self.sql_flights_dir}/count_pilots_assigned_to_flight.sql", (flight_id,))

    # ========================================
    # PILOT MANAGEMENT METHODS
    # ========================================

    def assign_pilot(self, pilot_id, flight_id, role):
        print("Assign Pilot to Flight")
        self.db.run_sql(f"{self.sql_pilots_dir}/assign_pilot.sql", (pilot_id, flight_id, role))

    def view_all_pilots(self):
        print("View All Pilots")
        self.db.run_sql(f"{self.sql_pilots_dir}/view_all_pilots.sql")

    def view_pilot_schedule(self, pilot_id):
        print("View Pilot Schedule")
        self.db.run_sql(f"{self.sql_pilots_dir}/view_pilot_schedule.sql", (pilot_id,))

    def view_pilots_by_role(self, role):
        print("View Pilots by Role")
        self.db.run_sql(f"{self.sql_pilots_dir}/view_pilot_by_role.sql", (role,))

    def summary_flights_per_pilot(self):
        print("Summary of Flights per Pilot")
        self.db.run_sql(f"{self.sql_pilots_dir}/summary_flights_per_pilot.sql")

    # ========================================
    # DESTINATION MANAGEMENT METHODS
    # ========================================

    def view_all_destinations(self):
        print("View All Destinations")
        self.db.run_sql(f"{self.sql_destinations_dir}/view_all_destinations.sql")
    
    def view_destination_by_country(self, country):
        print("View Destination by Country")
        self.db.run_sql(f"{self.sql_destinations_dir}/view_destination_by_country.sql", (country,))

    def update_destination(self, destination_id, name, country):
        print("Update Destination Information")
        self.db.run_sql(f"{self.sql_destinations_dir}/update_destination.sql", (name, country, destination_id))

    def count_flights_to_destination(self, destination_id):
        print("Count Flights to Destination")
        self.db.run_sql(f"{self.sql_destinations_dir}/count_flights_to_destinations.sql", (destination_id,))
    
    def count_flights_from_destination(self, departure_id):
        print("Count Flights from Destination")
        self.db.run_sql(f"{self.sql_destinations_dir}/count_flights_from_destination.sql", (departure_id,))

    # ========================================
    # BOOKING MANAGEMENT METHODS
    # ========================================

    def add_booking(self, flight_id, passenger_id, booking_date, booking_time, seat_number, travel_class):
        print("Add New Booking")
        self.db.run_sql(f"{self.sql_bookings_dir}/add_booking.sql", (flight_id, passenger_id, booking_date, booking_time, seat_number, travel_class))

    def view_all_bookings(self):
        print("View All Bookings")
        self.db.run_sql(f"{self.sql_bookings_dir}/view_all_bookings.sql")

    def view_bookings_for_flight(self, flight_id):
        print("View Bookings for Flight")
        self.db.run_sql(f"{self.sql_bookings_dir}/view_bookings_for_flight.sql", (flight_id,))

    def view_bookings_by_date(self, start_date, end_date=None):
        print("View Bookings by Date")
        if end_date is None:
            end_date = start_date # Query for a single day if no end_date
        self.db.run_sql(f"{self.sql_bookings_dir}/view_bookings_by_date.sql", (start_date, end_date))

    def view_passengers_on_flight(self, flight_id):
        print("View Passengers on Flight")
        self.db.run_sql(f"{self.sql_bookings_dir}/view_passengers_on_flight.sql", (flight_id,))

    def count_passengers_on_flight(self, flight_id):
        print("Count Passengers on Flight")
        self.db.run_sql(f"{self.sql_bookings_dir}/count_passengers_on_flight.sql", (flight_id,))

    # ========================================
    # PASSENGER MANAGEMENT METHODS
    # ========================================
    
    def add_passenger(self, name, nationality, date_of_birth):
        print("Add a New Passenger")
        self.db.run_sql(f"{self.sql_passengers_dir}/add_passenger.sql", (name, nationality, date_of_birth))

    def view_all_passengers(self):
        print("View All Passengers")
        self.db.run_sql(f"{self.sql_passengers_dir}/view_all_passengers.sql")
    
    def update_passenger_details(self, passenger_id, name, nationality, date_of_birth):
        print("Update Passenger Details")
        self.db.run_sql(f"{self.sql_passengers_dir}/update_passenger_details.sql", (name, nationality, date_of_birth, passenger_id))

    def view_passengers_by_nationality(self, nationality):
        print("View Passengers by Nationality")
        self.db.run_sql(f"{self.sql_passengers_dir}/view_passengers_by_nationality.sql", (nationality,))

    def add_luggage(self, tag_number, passenger_id, flight_id, weight):
        print("Add Luggage for Passenger")
        self.db.run_sql(f"{self.sql_passengers_dir}/add_luggage.sql", (tag_number, passenger_id, flight_id, weight))

    def view_luggage_for_passenger(self, passenger_id):
        print("View Luggage for Passenger")
        self.db.run_sql(f"{self.sql_passengers_dir}/view_luggage_for_passenger.sql", (passenger_id,))
