days = {"Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","Sunday","Sunday","Sunday"}

# remove friday and sunday from the set using methods

days.remove("Friday")
days.remove("Sunday")
print(days)


# Add them back to the set
days.add("Friday")
days.add("Sunday")

# OR
list = ["Friday", "Sunday","sunday","Sunday"]

days = days.update(list)
print(days)



