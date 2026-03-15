import random
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))
count = int(input("How many passwords to generate?: "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

passwords = []

for _ in range(count):

    password = []

    # ensure at least one of each
    password.append(random.choice(letters))
    password.append(random.choice(numbers))
    password.append(random.choice(symbols))

    for i in range(length - 3):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)

    passwords.append(final_password)


print("\nGenerated Passwords:")

for p in passwords:
    print(p)


# save passwords to file
save = input("\nSave passwords to file? (y/n): ")

if save == "y":

    with open("generated_passwords.txt", "w") as file:

        for p in passwords:
            file.write(p + "\n")

    print("Passwords saved to generated_passwords.txt")