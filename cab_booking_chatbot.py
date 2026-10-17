import random

# Predefined routes and distances
routes = {
    1: {
        "source": "Pune Station",
        "destination": "Shivajinagar",
        "distance": 5
    },
    2: {
        "source": "Swargate",
        "destination": "Kothrud",
        "distance": 8
    },
    3: {
        "source": "Hinjawadi",
        "destination": "Wakad",
        "distance": 10
    }
}

# Cab rates per kilometre
cab_rates = {
    1: {"name": "Auto", "rate": 12},
    2: {"name": "Sedan", "rate": 18},
    3: {"name": "SUV", "rate": 25}
}


def display_main_menu():
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")
    print("=========================================")


def choose_cab_type():
    while True:
        print("\n---------- Choose Cab Type ----------")
        print("1. Auto  - Rs. 12/km")
        print("2. Sedan - Rs. 18/km")
        print("3. SUV   - Rs. 25/km")

        try:
            choice = int(input("Enter your cab choice (1-3): "))

            if choice in cab_rates:
                return cab_rates[choice]

            print("Invalid choice! Please select 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def choose_route():
    while True:
        print("\n---------- Available Routes ----------")

        for number, route in routes.items():
            print(
                f"{number}. {route['source']} to "
                f"{route['destination']} "
                f"({route['distance']} km)"
            )

        try:
            choice = int(input("Choose your route (1-3): "))

            if choice in routes:
                return routes[choice]

            print("Invalid route! Please select 1, 2, or 3.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def calculate_fare(distance, rate):
    return distance * rate


def confirm_booking(route, cab, fare):
    while True:
        print("\n---------- Booking Summary ----------")
        print(f"Source      : {route['source']}")
        print(f"Destination : {route['destination']}")
        print(f"Cab Type    : {cab['name']}")
        print(f"Distance    : {route['distance']} km")
        print(f"Rate        : Rs. {cab['rate']}/km")
        print(f"Total Fare  : Rs. {fare}")

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        try:
            choice = int(input("Enter your choice (1-2): "))

            if choice == 1:
                return True

            elif choice == 2:
                print("\nRide cancelled successfully!")
                print("No OTP has been generated or shared.")
                return False

            else:
                print("Invalid choice! Please select 1 or 2.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def generate_otp():
    return random.randint(1000, 9999)


def book_ride():
    print("\n========== BOOK YOUR RIDE ==========")

    # Step 1: Choose cab
    cab = choose_cab_type()

    # Step 2: Choose route
    route = choose_route()

    # Step 3: Calculate fare
    distance = route["distance"]
    rate = cab["rate"]
    fare = calculate_fare(distance, rate)

    # Step 4: Confirm booking or cancel before OTP
    confirmed = confirm_booking(route, cab, fare)

    if not confirmed:
        return

    # Step 5: Generate and share OTP only after confirmation
    otp = generate_otp()

    print("\n========== BOOKING CONFIRMED ==========")
    print(f"Your OTP is: {otp}")
    print("Please share this OTP with the driver.")
    print("Your ride is now locked.")

    # Step 6: Cancellation is not allowed after OTP sharing
    print("\nCancellation is not allowed after OTP sharing.")
    print("Thank you for booking with us!")


def main():
    while True:
        display_main_menu()

        try:
            choice = int(input("Enter your choice (1-2): "))

            if choice == 1:
                book_ride()

            elif choice == 2:
                print("\nThank you for using the Cab Booking Chatbot!")
                print("Goodbye!")
                break

            else:
                print("Invalid menu choice! Please select 1 or 2.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Program execution starts here
if __name__ == "__main__":
    main()