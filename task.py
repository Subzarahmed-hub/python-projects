print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

# print("welcome to the tip calculator")
# Bill = float(input("what was the total bill?$"))
# Tip = int(input("How much tip would you like to give? 10, 12, or 15?$"))
# people = int(input("How many people to split the bill?$"))
# bill_with_tip = Tip / 100 * Bill + Bill
# Each_person_should_pay = (150.00/5)*1.12
# print(Each_person_should_pay)
# print(bill_with_tip)