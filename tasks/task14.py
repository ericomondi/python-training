# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them.
# The program should only accept numbers and floats only or
# otherwise display an error “invalid character entered” and
# take the user to re-enter the inputs .

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input")
else:
    total = num1 + num2

print(total)







    





