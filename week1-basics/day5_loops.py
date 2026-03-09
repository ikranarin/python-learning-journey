#Day 5 - Loops

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