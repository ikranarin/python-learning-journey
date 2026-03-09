#Day 5 - Loops

import random

# Print numbers 1-10
for i in range(1,11):
    print(i)

# Even numbers
for i in range(1,21):
    if i % 2 == 0:
        print(i)

# Multiplication table
number = int(input("Enter a number: "))

for i in range(1,11):
    print(number, "x", i, "=", number*i)

# Sum of numbers
total = 0

for i in range(1, 11):
    total = total + i

print("Total:", total)

#Number Guessing Game
secret_number = random.randint(1,10)

for i in range(3):
    guess = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("Correct!")
        break
    else:
        print("Wrong guess")

print("The secret number was:", secret_number)