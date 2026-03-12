# Day 6 - While Loops

# ----------------------------------
# 1. Basic while loop example
# ----------------------------------

print("Numbers from 1 to 5:")

i = 1
while i <= 5:
    print(i)
    i += 1


# ----------------------------------
# 2. Password check system
# ----------------------------------

print("\nPassword System")

password = ""

while password != "python123":
    password = input("Enter the password: ")

print("Access granted")


# ----------------------------------
# 3. Number guessing game
# ----------------------------------

import random

print("\nNumber Guessing Game")

secret_number = random.randint(1, 10)
guess = 0

while guess != secret_number:

    guess = int(input("Guess the number (1-10): "))

    if guess < secret_number:
        print("Too low")

    elif guess > secret_number:
        print("Too high")

print("Correct! 🎉 The number was:", secret_number)


# ----------------------------------
# 4. Simple menu system
# ----------------------------------

print("\nMenu System")

choice = ""

while choice != "q":

    print("\n1 - Say Hello")
    print("2 - Say Bye")
    print("q - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello!")

    elif choice == "2":
        print("Bye!")

print("Program ended")