# MOSES MWAI WAHOME
# SCT211-0029/2022
from datetime import date


# Request year of birth from user
yob = int(input("Enter your year of birth: "))

# Get current date 
year, month, day =  str(date.today()).split('-')
age = int(year) - yob
print("You are {} years, {} months and {} days old.".format(age, int(month), int(day)))
