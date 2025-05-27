from client import Client
from database import Database


def cli(db_name="flight"):
    """Command Line Interface for the Flight Management System."""

    db = Database(db_name)
    client = Client(db)

    def _print_menu_opts(opts):
        """Print menu options with numbers."""
        for i, opt in enumerate(opts, start=1):
            print(f"{i}. {opt}")

    def _get_input(prompt, input_type=str):
        """Get input with basic type conversion."""
        try:
            value = input(prompt)
            if input_type == int:
                return int(value)
            elif input_type == float:
                return float(value)
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
            return _get_input(prompt, input_type)

    def flight_management_menu():
        """Flight Management submenu."""
        while True:
            print("\n=== FLIGHT MANAGEMENT ===")
            flight_opts = [
                "Add New Flight",
                "View All Flights", 
                "View Flights by Departure",
                "View Flights by Destination",
                "View Flights by Duration",
                "View Flights by Price Range",
                "View Flights by Date",
                "View Flights by Status",
                "Update Flight Information",
                "Update Flight Status",
                "Update Flight Departure Time",
                "Summary: Flights per Destination",
                "Count Pilots Assigned to Flight",
                "Back to Main Menu"
            ]
            _print_menu_opts(flight_opts)
            
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    departure_airport_id = _get_input("Enter departure airport ID: ", int)
                    destination_airport_id = _get_input("Enter destination airport ID: ", int)
                    duration = _get_input("Enter duration (minutes): ", int)
                    price = _get_input("Enter price: ", float)
                    status = _get_input("Enter status (Scheduled/Delayed/Cancelled): ")
                    departure_datetime = _get_input("Enter departure datetime (YYYY-MM-DD HH:MM:SS): ")
                    client.add_flight(departure_airport_id, destination_airport_id, duration, price, status, departure_datetime)
                case "2":
                    client.view_all_flights()
                case "3":
                    departure_id = _get_input("Enter departure airport ID: ", int)
                    client.view_flights_by_departure(departure_id)
                case "4":
                    destination_id = _get_input("Enter destination airport ID: ", int)
                    client.view_flights_by_destination(destination_id)
                case "5":
                    max_duration = _get_input("Enter maximum duration (minutes): ", int)
                    client.view_flights_by_duration(max_duration)
                case "6":
                    min_price = _get_input("Enter minimum price: ", float)
                    max_price = _get_input("Enter maximum price: ", float)
                    client.view_flights_by_price_range(min_price, max_price)
                case "7":
                    departure_date = _get_input("Enter departure date (YYYY-MM-DD): ")
                    client.view_flights_by_date(departure_date)
                case "8":
                    status = _get_input("Enter status (Scheduled/Delayed/Cancelled): ")
                    client.view_flights_by_status(status)
                case "9":
                    flight_id = _get_input("Enter flight ID: ", int)
                    departure_airport_id = _get_input("Enter new departure airport ID: ", int)
                    destination_airport_id = _get_input("Enter new destination airport ID: ", int)
                    duration = _get_input("Enter new duration (minutes): ", int)
                    price = _get_input("Enter new price: ", float)
                    client.update_flight(flight_id, departure_airport_id, destination_airport_id, duration, price)
                case "10":
                    flight_id = _get_input("Enter flight ID: ", int)
                    new_status = _get_input("Enter new status (Scheduled/Delayed/Cancelled): ")
                    client.update_flight_status(flight_id, new_status)
                case "11":
                    flight_id = _get_input("Enter flight ID: ", int)
                    new_departure_datetime = _get_input("Enter new departure datetime (YYYY-MM-DD HH:MM:SS): ")
                    client.update_flight_departure_time(flight_id, new_departure_datetime)
                case "12":
                    client.summary_flights_per_destination()
                case "13":
                    flight_id = _get_input("Enter flight ID: ", int)
                    client.count_pilots_assigned_to_flight(flight_id)
                case "14":
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def pilot_management_menu():
        """Pilot Management submenu."""
        while True:
            print("\n=== PILOT MANAGEMENT ===")
            pilot_opts = [
                "View All Pilots",
                "Assign Pilot to Flight",
                "View Pilot Schedule",
                "View Pilots by Role",
                "Summary: Flights per Pilot",
                "Back to Main Menu"
            ]
            _print_menu_opts(pilot_opts)
            
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    client.view_all_pilots()
                case "2":
                    pilot_id = _get_input("Enter pilot ID: ", int)
                    flight_id = _get_input("Enter flight ID: ", int)
                    role = _get_input("Enter pilot role (Captain/First Officer/etc.): ")
                    client.assign_pilot(pilot_id, flight_id, role)
                case "3":
                    pilot_id = _get_input("Enter pilot ID: ", int)
                    client.view_pilot_schedule(pilot_id)
                case "4":
                    role = _get_input("Enter role to filter by: ")
                    client.view_pilots_by_role(role)
                case "5":
                    client.summary_flights_per_pilot()
                case "6":
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def destination_management_menu():
        """Destination Management submenu."""
        while True:
            print("\n=== DESTINATION MANAGEMENT ===")
            destination_opts = [
                "View All Destinations",
                "View Destinations by Country",
                "Update Destination Information",
                "Count Flights to Destination",
                "Count Flights from Destination",
                "Back to Main Menu"
            ]
            _print_menu_opts(destination_opts)
            
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    client.view_all_destinations()
                case "2":
                    country = _get_input("Enter country name: ")
                    client.view_destination_by_country(country)
                case "3":
                    destination_id = _get_input("Enter destination/airport ID: ", int)
                    name = _get_input("Enter new airport name: ")
                    country = _get_input("Enter new country: ")
                    client.update_destination(destination_id, name, country)
                case "4":
                    destination_id = _get_input("Enter destination airport ID: ", int)
                    client.count_flights_to_destination(destination_id)
                case "5":
                    departure_id = _get_input("Enter departure airport ID: ", int)
                    client.count_flights_from_destination(departure_id)
                case "6":
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def booking_management_menu():
        """Booking Management submenu."""
        while True:
            print("\n=== BOOKING MANAGEMENT ===")
            booking_opts = [
                "Add New Booking",
                "View All Bookings",
                "View Bookings for Flight",
                "View Bookings by Date",
                "View Passengers on Flight",
                "Count Passengers on Flight",
                "Back to Main Menu"
            ]
            _print_menu_opts(booking_opts)
            
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    flight_id = _get_input("Enter flight ID: ", int)
                    passenger_id = _get_input("Enter passenger ID: ", int)
                    booking_date = _get_input("Enter booking date (YYYY-MM-DD): ")
                    booking_time = _get_input("Enter booking time (HH:MM): ")
                    seat_number = _get_input("Enter seat number: ")
                    travel_class = _get_input("Enter travel class (Economy/Business/First): ")
                    client.add_booking(flight_id, passenger_id, booking_date, booking_time, seat_number, travel_class)
                case "2":
                    client.view_all_bookings()
                case "3":
                    flight_id = _get_input("Enter flight ID: ", int)
                    client.view_bookings_for_flight(flight_id)
                case "4":
                    start_date = _get_input("Enter start date (YYYY-MM-DD): ")
                    end_date_input = _get_input("Enter end date (YYYY-MM-DD) or press Enter for single day: ")
                    end_date = end_date_input if end_date_input.strip() else None
                    client.view_bookings_by_date(start_date, end_date)
                case "5":
                    flight_id = _get_input("Enter flight ID: ", int)
                    client.view_passengers_on_flight(flight_id)
                case "6":
                    flight_id = _get_input("Enter flight ID: ", int)
                    client.count_passengers_on_flight(flight_id)
                case "7":
                    break
                case _:
                    print("Invalid choice. Please try again.")

    def passenger_management_menu():
        """Passenger Management submenu."""
        while True:
            print("\n=== PASSENGER MANAGEMENT ===")
            passenger_opts = [
                "Add New Passenger",
                "View All Passengers",
                "Update Passenger Details",
                "View Passengers by Nationality",
                "Add Luggage for Passenger",
                "View Luggage for Passenger",
                "Back to Main Menu"
            ]
            _print_menu_opts(passenger_opts)
            
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    name = _get_input("Enter passenger name: ")
                    nationality = _get_input("Enter nationality: ")
                    date_of_birth = _get_input("Enter date of birth (YYYY-MM-DD): ")
                    client.add_passenger(name, nationality, date_of_birth)
                case "2":
                    client.view_all_passengers()
                case "3":
                    passenger_id = _get_input("Enter passenger ID: ", int)
                    name = _get_input("Enter new name: ")
                    nationality = _get_input("Enter new nationality: ")
                    date_of_birth = _get_input("Enter new date of birth (YYYY-MM-DD): ")
                    client.update_passenger_details(passenger_id, name, nationality, date_of_birth)
                case "4":
                    nationality = _get_input("Enter nationality to filter by: ")
                    client.view_passengers_by_nationality(nationality)
                case "5":
                    tag_number = _get_input("Enter luggage tag number: ")
                    passenger_id = _get_input("Enter passenger ID: ", int)
                    flight_id = _get_input("Enter flight ID: ", int)
                    weight = _get_input("Enter weight (kg): ", float)
                    client.add_luggage(tag_number, passenger_id, flight_id, weight)
                case "6":
                    passenger_id = _get_input("Enter passenger ID: ", int)
                    client.view_luggage_for_passenger(passenger_id)
                case "7":
                    break
                case _:
                    print("Invalid choice. Please try again.")

    # Main menu loop
    while True:
        print("\n" + "="*50)
        print("    FLIGHT MANAGEMENT SYSTEM")
        print("="*50)
        menu_opts = [
            "Flight Management",
            "Pilot Management", 
            "Destination Management",
            "Booking Management",
            "Passenger Management",
            "Exit"
        ]
        _print_menu_opts(menu_opts)

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                flight_management_menu()
            case "2":
                pilot_management_menu()
            case "3":
                destination_management_menu()
            case "4":
                booking_management_menu()
            case "5":
                passenger_management_menu()
            case "6":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cli()