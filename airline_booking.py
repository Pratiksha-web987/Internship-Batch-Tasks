# Task 11: Airline Ticket Booking System

# Function to calculate the base ticket price
def calculateBaseFare(ticket_price, number_of_tickets):
    return ticket_price * number_of_tickets


# Function to calculate the booking fee
def calculateBookingFee(base_fare, fee_percentage):
    return base_fare * fee_percentage / 100


# Function to calculate GST on the ticket fare
def calculateGST(base_fare, gst_percentage):
    return base_fare * gst_percentage / 100


# Function to calculate the total booking amount
def calculateTotalAmount(base_fare, booking_fee, gst):
    return base_fare + booking_fee + gst


# Function to apply a discount to the total amount
def calculateDiscount(total_amount, discount_percentage):
    return total_amount * discount_percentage / 100


# Function to calculate the final payable amount
def calculateFinalAmount(total_amount, discount):
    return total_amount - discount


# Given booking details
passenger_name = "Rahul Sharma"
source = "Pune"
destination = "Delhi"
ticket_price = 5000
number_of_tickets = 2

booking_fee_percentage = 5
gst_percentage = 5
discount_percentage = 10


# Calculate the base fare
base_fare = calculateBaseFare(
    ticket_price,
    number_of_tickets
)

# Calculate the booking fee
booking_fee = calculateBookingFee(
    base_fare,
    booking_fee_percentage
)

# Calculate GST on the base fare
gst = calculateGST(
    base_fare,
    gst_percentage
)

# Calculate the total amount before discount
total_amount = calculateTotalAmount(
    base_fare,
    booking_fee,
    gst
)

# Calculate the discount
discount = calculateDiscount(
    total_amount,
    discount_percentage
)

# Calculate the final payable amount
final_amount = calculateFinalAmount(
    total_amount,
    discount
)


# Display the booking details
print("===== AIRLINE TICKET BOOKING =====")
print("Passenger Name:", passenger_name)
print("Source:", source)
print("Destination:", destination)
print("Number of Tickets:", number_of_tickets)

print("----------------------------------")
print("Base Fare: Rs.", round(base_fare, 2))
print("Booking Fee: Rs.", round(booking_fee, 2))
print("GST: Rs.", round(gst, 2))
print("Total Amount: Rs.", round(total_amount, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Payable Amount: Rs.", round(final_amount, 2))
print("----------------------------------")
print("Thank you for booking with us!")
