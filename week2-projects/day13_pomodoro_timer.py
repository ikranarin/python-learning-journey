import time

WORK_TIME = 25 * 60
BREAK_TIME = 5 * 60


def countdown(seconds, label):
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{label} {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"{label} DONE!          ")


def pomodoro():
    while True:
        print("\nWork Time Started!")
        countdown(WORK_TIME, "Work")

        print("\nBreak Time Started!")
        countdown(BREAK_TIME, "Break")

        cont = input("\nContinue? (y/n): ").lower()
        if cont != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    pomodoro()