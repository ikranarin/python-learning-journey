#Day 4 - Simple Login System

username = input("Enter username: ")
password = input("Enter password: ")

if len(password) < 3:
    print("Password too short")

if username == "admin" and password == "1234":
    print("Login successful")

elif username != "admin":
    print("Username not found")

elif password != "1234":
    print("Wrong password")