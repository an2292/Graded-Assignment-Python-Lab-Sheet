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
                        "View Flights by Depature Date",
                        "View Flights by Passenger Count",
                        "View Flights by Pilot Count",
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
                            date = input("Enter date: ")
                            client.view_flights_by_date(date)
                        case "6":
                            flight_id = input("Enter flight ID: ")
                            client.count_passengers_on_flight(flight_id)
                        case "7":
                            flight_id = input("Enter flight ID: ")
                            client.count_pilots_assigned_to_flight(flight_id)
                        case "8":
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
    cli()