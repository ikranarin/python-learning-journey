# Day 7 - ATM Simulation

balance = 1000

choice = ""

while choice != "4":

    print("\n--- ATM MENU ---")
    print("1 - Check Balance")
    print("2 - Deposit Money")
    print("3 - Withdraw Money")
    print("4 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print("Deposit successful")

    elif choice == "3":
        withdraw = float(input("Enter amount to withdraw: "))

        if withdraw > balance:
            print("Insufficient balance")

        else:
            balance -= withdraw
            print("Withdrawal successful")

    elif choice == "4":
        print("Thank you for using the ATM")

    else:
        print("Invalid option")