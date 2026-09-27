print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill?\n"))
people = int(input("How many people to split the bill?\n"))
tip = float(input("What percentage tip would you like to give?\n"))

total = bill * (1 + tip / 100)
bill_per_person = total / people

print(f"Each person should pay: ${bill_per_person:.2f}")