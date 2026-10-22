# Kiran Academy - Task 13
# Banking Console Application

print("Welcome to Kiran Bank")

balance = 10000.00
print(f"Opening Balance: Rs. {balance:.0f}")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        print(f"Current Balance: Rs. {balance:g}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Transaction failed: Amount must be greater than zero.")
            else:
                balance += amount
                print("Deposit successful.")
                print(f"Updated Balance: Rs. {balance:g}")

        except ValueError:
            print("Transaction failed: Please enter a valid amount.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Transaction failed: Amount must be greater than zero.")
            elif amount > balance:
                print("Transaction failed: Insufficient balance.")
            else:
                balance -= amount
                print("Withdrawal successful.")
                print(f"Updated Balance: Rs. {balance:g}")

        except ValueError:
            print("Transaction failed: Please enter a valid amount.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")