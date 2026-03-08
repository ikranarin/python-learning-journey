#Day 4 - Simple Login System

username = input("Enter username: ")
password = input("Enter password: ")

if any(char.isdigit() for char in password):
    print("Your password is valid.")
else:
    print("Password must contain a number.")

if len(password) < 3:
    print("Password too short")

if username == "admin" and password == "1234":
    print("Login successful")

elif username != "admin":
    print("Username not found")

elif password != "1234":
    print("Wrong password")

#OR Example

age = int(input("Enter your age: "))

if age < 18 or age > 65:
    print("You are in a special age group")
else:
    print("Standard age group")

#NOT Example

is_logged_in = False

if not is_logged_in:
    print("Please log in first")