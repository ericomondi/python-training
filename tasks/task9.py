# Write a program called stars. It should prompt the user
#  for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.
# for i in range(0,6):
#     print("*" * i)

num = int(input("Enter the no of rows required: "))
rows = num + 1
for n in range(0,rows):
    print("*" * n)
