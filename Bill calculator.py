#Tip Calculator
print ("Welcome to the tip calculator")
bill = (float(input("What was the total bill? £")))
tip = (int(input("What percentage would you like to tip? 10, 12, 15? ")))
people = (int(input("How many people would you like to split the bill between? ")))

tip_percentage = (tip / 100)
total_tip =  tip_percentage * bill 
total_bill = (round(bill + total_tip,2))
per_person = (round(total_bill/people,2))

total_bill_2sf = "{:.2f}".format(total_bill)
per_person_2sf = "{:.2f}".format(per_person)

print (f"Your total bill is £{total_bill_2sf}")
print (f"This split between {people} people, comes to £{per_person_2sf} each")
