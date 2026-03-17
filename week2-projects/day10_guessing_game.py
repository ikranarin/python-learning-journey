import random
import json

# -----------------------------
# LOAD DATA
# -----------------------------
try:
    with open("game_data.json", "r") as file:
        data = json.load(file)
except:
    data = {
        "highscore": 0,
        "wins": 0,
        "losses": 0
    }

# -----------------------------
# FUNCTIONS
# -----------------------------

def save_data():
    with open("game_data.json", "w") as file:
        json.dump(data, file)


def player_mode():

    print("\n=== PLAYER MODE ===")

    max_number = 100
    attempts = 10

    secret = random.randint(1, max_number)
    score = 0

    for i in range(attempts):

        guess = int(input("Your guess: "))
        diff = abs(secret - guess)

        if guess == secret:
            score = (attempts - i) * 10
            print("🎉 Correct!")
            break

        elif guess < secret:
            print("Too low")
        else:
            print("Too high")

        if diff <= 3:
            print("VERY CLOSE")
        elif diff <= 10:
            print("Close")
        else:
            print("Far")

        print(f"Remaining attempts: {attempts - i - 1}")

    else:
        print(f"\n💀 Lost! Number was {secret}")
        data["losses"] += 1
        save_data()
        return

    print(f"Score: {score}")

    data["wins"] += 1

    if score > data["highscore"]:
        print("🏆 NEW HIGH SCORE!")
        data["highscore"] = score

    save_data()


def ai_mode():

    print("\n=== AI MODE ===")

    low = 1
    high = 100

    secret = int(input("Pick a number (1-100): "))

    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1

        print(f"AI guesses: {guess}")

        if guess == secret:
            print(f"🤖 AI found it in {attempts} steps!")
            break

        elif guess < secret:
            print("Going higher...")
            low = guess + 1
        else:
            print("Going lower...")
            high = guess - 1


def show_stats():
    print("\n=== STATS ===")
    print("Wins:", data["wins"])
    print("Losses:", data["losses"])
    print("High Score:", data["highscore"])


# -----------------------------
# MAIN LOOP
# -----------------------------

while True:

    print("\n=== MAIN MENU ===")
    print("1 - Play")
    print("2 - AI Mode")
    print("3 - Stats")
    print("4 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        player_mode()

    elif choice == "2":
        ai_mode()

    elif choice == "3":
        show_stats()

    elif choice == "4":
        print("Thanks for playing! Goodbye!")
        break

    else:
        print("Invalid choice")