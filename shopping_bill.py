# Task 01: Shopping Bill - GST First, Discount After

# Function to calculate the electronics bill after 18% GST
def calculateElectronicsGST(amount):
    gst = amount * 18 / 100
    return amount + gst


# Function to calculate the fashion bill after 13% GST
def calculateFashionGST(amount):
    gst = amount * 13 / 100
    return amount + gst


# Function to calculate the food bill after 7% GST
def calculateFoodGST(amount):
    gst = amount * 7 / 100
    return amount + gst


# Function to calculate the total bill after GST
def totalBill(electronics, fashion, food):
    return electronics + fashion + food


# Function to apply a 20% discount to the total bill
def calculateDiscountedBill(total):
    discount = total * 20 / 100
    return total - discount


# Given item prices
a = 100
b = 100
c = 100
d = 100
e = 100


# Calculate the electronics bill after GST
electronicsBill = calculateElectronicsGST(a + b)

# Calculate the fashion bill after GST
fashionBill = calculateFashionGST(c + d)

# Calculate the food bill after GST
foodBill = calculateFoodGST(e)


# Calculate the total bill after GST
total = totalBill(
    electronicsBill,
    fashionBill,
    foodBill
)


# Apply a 20% discount to the total bill
finalBill = calculateDiscountedBill(total)


# Display the final bill details
print("Electronics Bill after GST:", round(electronicsBill, 2))
print("Fashion Bill after GST:", round(fashionBill, 2))
print("Food Bill after GST:", round(foodBill, 2))
print("Total Bill after GST:", round(total, 2))
print("Discount: 20%")
print("Final Bill after Discount:", round(finalBill, 2))