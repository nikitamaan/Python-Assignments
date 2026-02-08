# Simple Tip Calculator

print(" Tip Calculator")
bill = float(input("What was the total bill? $"))

tip_percent = int(input("How much tip would you like to give? (percent) "))

people = int(input("How many people to split the bill? "))

tip_as_decimal = tip_percent / 100
total_tip_amount = bill * tip_as_decimal
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")