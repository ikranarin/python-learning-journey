# Day 7 - ATM Simulation (Advanced)

balance = 1000
correct_pin = "1234"
transactions = []
max_attempts = 3
attempts = 0

# -----------------------------
# PIN verification with limit
# -----------------------------

while attempts < max_attempts:

    entered_pin = input("Enter your ATM PIN: ")

    if entered_pin == correct_pin:
        print("PIN accepted. Welcome!")
        break

    else:
        attempts += 1
        print("Wrong PIN.")

        if attempts < max_attempts:
            print("Try again.\n")

else:
    print("Your card has been blocked.")
    exit()

# -----------------------------
# ATM MENU
# -----------------------------

choice = ""

while choice != "5":

    print("\n--- ATM MENU ---")
    print("1 - Check Balance")
    print("2 - Deposit Money")
    print("3 - Withdraw Money")
    print("4 - Transaction History")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":

        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        transactions.append(f"Deposited: {deposit}")

        print("Deposit successful")
        print("New balance:", balance)

    elif choice == "3":

        withdraw = float(input("Enter amount to withdraw: "))
        withdraw_limit = 500

        if withdraw > withdraw_limit:
            print("Withdrawal limit is 500")

        elif withdraw > balance:
            print("Insufficient balance")

        else:
            balance -= withdraw
            transactions.append(f"Withdrew: {withdraw}")

            print("Withdrawal successful")
            print("New balance:", balance)

    elif choice == "4":

        print("\nTransaction History:")

        if len(transactions) == 0:
            print("No transactions yet")

        else:
            for t in transactions:
                print("-", t)

    elif choice == "5":

        print("\n--- RECEIPT ---")
        print("Final balance:", balance)

        print("\nTransactions:")
        if len(transactions) == 0:
            print("No transactions")

        else:
            for t in transactions:
                print("-", t)

        print("\nThank you for using the ATM")

    else:
        print("Invalid option")