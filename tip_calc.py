# MOSES MWAI WAHOME
# SCT211/0029/2022

bill_amount = int(input("Enter the total bill amount: "))
tip_amount = int(input("Enter the tip amount(10, 12, or 15): "))
no_of_people = int(input("Enter the number of people splitting the bill: "))

tip = (bill_amount * tip_amount) / 100
total_bill = bill_amount + tip

print("Each person should pay ksh.{:.2f}.".format(total_bill / no_of_people))