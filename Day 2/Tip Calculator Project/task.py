print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip_percent=float(bill*tip/100)
final_bill=(tip_percent+bill)
per_person_payout=float(final_bill/people)
print(f"Each person should pay {per_person_payout}",2)