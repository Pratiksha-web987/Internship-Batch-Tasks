from abc import ABC, abstractmethod
import uuid


# FLIGHT CLASS 
class Flight:
    def __init__(self, code, airline, source, destination,
                 available_seats, base_fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.__available_seats = available_seats
        self.base_fare = base_fare

    @property
    def available_seats(self):
        return self.__available_seats

    def reserve_seats(self, count):
        if 0 < count <= self.__available_seats:
            self.__available_seats -= count
            return True
        return False

    def display(self):
        print(
            f"{self.code:<8} {self.airline:<15} "
            f"{self.source:<12} {self.destination:<12} "
            f"{self.available_seats:<8} "
            f"Rs.{self.base_fare:.2f}"
        )


#  ABSTRACT PASSENGER CLASS
class Passenger(ABC):
    def __init__(self, name, age):
        if not name.strip():
            raise ValueError("Passenger name cannot be empty.")
        if not 1 <= age <= 120:
            raise ValueError("Age must be between 1 and 120.")

        self.name = name.strip()
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


# INHERITANCE 
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 15


# BOOKING CLASS 
class Booking:
    def __init__(self, passenger, flight, tickets):
        self.booking_id = "BK" + uuid.uuid4().hex[:8].upper()
        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets

        self.base_total = flight.base_fare * tickets
        self.discount_percent = passenger.get_discount()
        self.discount_amount = (
            self.base_total * self.discount_percent / 100
        )
        self.final_total = self.base_total - self.discount_amount

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID       :", self.booking_id)
        print("Passenger Name   :", self.passenger.name)
        print("Passenger Age    :", self.passenger.age)
        print("Passenger Type   :", type(self.passenger).__name__)
        print("Flight Code      :", self.flight.code)
        print("Airline          :", self.flight.airline)
        print("Route            :", self.flight.source,
              "to", self.flight.destination)
        print("Number of Tickets:", self.tickets)
        print(f"Base Fare Total  : Rs.{self.base_total:.2f}")
        print(f"Discount         : {self.discount_percent}%")
        print(f"Discount Amount  : Rs.{self.discount_amount:.2f}")
        print(f"Final Amount     : Rs.{self.final_total:.2f}")
        print("======================================")


# FLIGHT BOOKING SYSTEM 
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("AI101", "Air India", "Mumbai", "Delhi", 40, 5200),
            Flight("6E202", "IndiGo", "Pune", "Bengaluru", 35, 4100),
            Flight("UK303", "Vistara", "Delhi", "Chennai", 25, 6800),
        ]
        self.bookings = []
        self.recent_booking = None

    def view_flights(self):
        print("\n================ AVAILABLE FLIGHTS ================")
        print(
            f"{'Code':<8} {'Airline':<15} {'Source':<12} "
            f"{'Destination':<12} {'Seats':<8} Base Fare"
        )
        print("-" * 75)

        for flight in self.flights:
            flight.display()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code == code.upper():
                return flight
        return None

    def read_integer(self, message, minimum, maximum):
        while True:
            try:
                value = int(input(message))
                if minimum <= value <= maximum:
                    return value
                print(f"Enter a number from {minimum} to {maximum}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def book_flight(self):
        self.view_flights()

        code = input("\nEnter flight code: ").strip().upper()
        flight = self.find_flight(code)

        if flight is None:
            print("Error: Flight not found.")
            return

        if flight.available_seats == 0:
            print("Sorry, this flight is fully booked.")
            return

        name = input("Enter passenger name: ").strip()
        if not name:
            print("Error: Passenger name cannot be empty.")
            return

        age = self.read_integer("Enter passenger age (1-120): ", 1, 120)

        print("\nPassenger Category")
        print("1. Regular Passenger (0% discount)")
        print("2. Student Passenger (15% discount)")

        category = self.read_integer("Choose category (1-2): ", 1, 2)

        tickets = self.read_integer(
            f"Enter number of tickets (1-{flight.available_seats}): ",
            1,
            flight.available_seats
        )

        if category == 1:
            passenger = RegularPassenger(name, age)
        else:
            passenger = StudentPassenger(name, age)

        booking = Booking(passenger, flight, tickets)

        print("\n========== FARE DETAILS ==========")
        print(f"Base Fare     : Rs.{booking.base_total:.2f}")
        print(f"Discount      : Rs.{booking.discount_amount:.2f}")
        print(f"Final Fare    : Rs.{booking.final_total:.2f}")

        confirm = input("Confirm booking? (Y/N): ").strip().upper()

        if confirm != "Y":
            print("Booking cancelled. No seats were reserved.")
            return

        if not flight.reserve_seats(tickets):
            print("Booking failed. Seats are no longer available.")
            return

        self.bookings.append(booking)
        self.recent_booking = booking

        print("\nBooking confirmed successfully!")
        booking.display_summary()

    def view_booking(self):
        if self.recent_booking is None:
            print("\nNo confirmed booking found.")
        else:
            self.recent_booking.display_summary()

    def run(self):
        print("\nWelcome to the Flight Booking System!")

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                self.view_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("Thank you for using the Flight Booking System!")
                break

            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")


# MAIN PROGRAM 
if __name__ == "__main__":
    try:
        system = FlightBookingSystem()
        system.run()
    except (KeyboardInterrupt, EOFError):
        print("\nApplication closed. Goodbye!")