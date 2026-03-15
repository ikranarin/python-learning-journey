import random
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))
use_numbers = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = list(string.ascii_letters)

if use_numbers == "y":
    characters += list(string.digits)

if use_symbols == "y":
    characters += list(string.punctuation)

password = []

for i in range(length):
    password.append(random.choice(characters))

random.shuffle(password)

final_password = "".join(password)

print("\nGenerated password:")
print(final_password)