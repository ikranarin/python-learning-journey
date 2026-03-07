#Day 3 - Conditions

number1 = int(input("Enter a number: "))

if number1 > 0:
    print("The number is positive.")

number2 = int(input("Enter a number: "))

if number2 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Grading System

grade = int(input("Enter your exam score: "))
if grade >= 90:
    print("Your grade is A.")
elif grade >= 80:
    print("Your grade is B.")
elif grade >= 70:
    print("Your grade is C.")
elif grade >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")