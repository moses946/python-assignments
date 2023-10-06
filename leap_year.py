# MOSES MWAI WAHOME
# SCT211-0029/2022

year  = int(input("Enter an year to check if it is a leap year: "))

if (year % 4 == 0):
    print("{} is a leap year.".format(str(year)))
else:
    print("{} is not a leap year.".format(str(year)))