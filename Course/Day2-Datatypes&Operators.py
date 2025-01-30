# print(type(12334))
# print(type("12334"))
# print(type(123.34))
# print(type(True))

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? ")) / 100
split = int(input("How many people to split the bill?"))

print("Each person should pay: $" + str(round(((total_bill * tip_percentage) + total_bill) / split, 2)))
