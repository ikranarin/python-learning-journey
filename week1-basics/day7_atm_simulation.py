# Day 7 - Advanced ATM Simulation

balance = 1000
correct_pin = "1234"
transactions = []

max_attempts = 3
attempts = 0


# -----------------------------
# PIN verification
# -----------------------------

while attempts < max_attempts:

    entered_pin = input("Enter your ATM PIN: ")

    if entered_pin == correct_pin:
        print("PIN accepted. Welcome!")
        break

    else:
        attempts += 1
        print("Wrong PIN")

        if attempts < max_attempts:
            print("Try again\n")

else:
    print("Your card has been blocked.")
    exit()


# -----------------------------
# ATM MENU
# -----------------------------

choice = ""

while choice != "7":

    print("\n--- ATM MENU ---")
    print("1 - Check Balance")
    print("2 - Deposit Money")
    print("3 - Withdraw Money")
    print("4 - Transfer Money")
    print("5 - Transaction History")
    print("6 - Change PIN")
    print("7 - Exit")

    choice = input("Choose an option: ")

    # -----------------------------
    # Check Balance
    # -----------------------------

    if choice == "1":

        print("Your balance:", balance)

    # -----------------------------
    # Deposit
    # -----------------------------

    elif choice == "2":

        deposit = float(input("Enter deposit amount: "))

        if deposit <= 0:
            print("Invalid amount")

        else:
            balance += deposit
            transactions.append(f"Deposited {deposit}")
            print("Deposit successful")
            print("New balance:", balance)

    # -----------------------------
    # Withdraw
    # -----------------------------

    elif choice == "3":

        withdraw = float(input("Enter withdraw amount: "))
        withdraw_limit = 500

        if withdraw <= 0:
            print("Invalid amount")

        elif withdraw > withdraw_limit:
            print("Withdrawal limit is 500")

        elif withdraw > balance:
            print("Insufficient balance")

        else:
            balance -= withdraw
            transactions.append(f"Withdrew {withdraw}")
            print("Withdrawal successful")
            print("New balance:", balance)

    # -----------------------------
    # Transfer
    # -----------------------------

    elif choice == "4":

        account = input("Enter receiver account number: ")
        amount = float(input("Enter transfer amount: "))

        if amount <= 0:
            print("Invalid amount")

        elif amount > balance:
            print("Insufficient balance")

        else:
            balance -= amount
            transactions.append(f"Transferred {amount} to {account}")
            print("Transfer successful")
            print("New balance:", balance)

    # -----------------------------
    # Transaction History
    # -----------------------------

    elif choice == "5":

        print("\nTransaction History")

        if len(transactions) == 0:
            print("No transactions yet")

        else:
            for t in transactions:
                print("-", t)

    # -----------------------------
    # Change PIN
    # -----------------------------

    elif choice == "6":

        old_pin = input("Enter current PIN: ")

        if old_pin == correct_pin:

            new_pin = input("Enter new PIN: ")
            correct_pin = new_pin

            print("PIN changed successfully")

        else:
            print("Wrong PIN")

    # -----------------------------
    # Exit
    # -----------------------------

    elif choice == "7":

        confirm = input("Are you sure you want to exit? (y/n): ")

        if confirm == "y":

            print("\n--- RECEIPT ---")
            print("Final balance:", balance)

            print("\nTransactions:")
            if len(transactions) == 0:
                print("No transactions")
            else:
                for t in transactions:
                    print("-", t)

            print("\nThank you for using the ATM")
            break

        elif confirm == "n":
            print("Returning to menu...")
            choice = ""  # menüye kesin dönüş

        else:
            print("Invalid input")