import random

print("=== NUMBER GUESSING GAME ===")

while True:

    print("\nSelect Difficulty:")
    print("1 - Easy (1-10, 5 attempts)")
    print("2 - Medium (1-50, 7 attempts)")
    print("3 - Hard (1-100, 10 attempts)")

    difficulty = input("Choose: ")

    if difficulty == "1":
        max_number = 10
        attempts = 5
    elif difficulty == "2":
        max_number = 50
        attempts = 7
    elif difficulty == "3":
        max_number = 100
        attempts = 10
    else:
        print("Invalid choice")
        continue

    secret_number = random.randint(1, max_number)

    print(f"\nI picked a number between 1 and {max_number}")

    for i in range(attempts):

        guess = int(input("Enter your guess: "))

        diff = abs(secret_number - guess)

        if guess == secret_number:
            print("🎉 Correct! You win!")
            break

        elif guess < secret_number:
            print("Too low")

        else:
            print("Too high")

        # Hint system
        if diff <= 3:
            print("🔥 Very close!")
        elif diff <= 10:
            print("🙂 Close")
        else:
            print("❄️ Far")

        print(f"Remaining attempts: {attempts - i - 1}")

    else:
        print(f"\n💀 You lost! The number was {secret_number}")

    # play again
    again = input("\nPlay again? (y/n): ")

    if again != "y":
        print("Thanks for playing!")
        break